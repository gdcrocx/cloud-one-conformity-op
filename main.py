from os import walk, stat
from cto_ai import ux, prompt, sdk

import json
import urllib3

def postConformityApi(ccApiKey, fileString):

    headers = {
        "Content-Type": "application/vnd.api+json",
        "Authorization": "ApiKey " + ccApiKey
    }

    data = {
        "data": {
            "attributes": {
                "type": "cloudformation-template",
                "contents": fileString
            }
        }
    }

    http = urllib3.PoolManager()

    r = http.request('POST', 'https://us-west-2-api.cloudconformity.com/v1/template-scanner/scan', headers=headers, body=json.dumps(data))
    
    responseDict = json.loads(r.data)
    
    sdk.log(responseDict)    
    
    reportDict = {}

    for data in responseDict["data"]:
        if data["type"] == "checks":
            if str(data["attributes"]["risk-level"]) not in reportDict:
                reportDict.update({ data["attributes"]["risk-level"]: 1 })
            else:
                reportDict.update({ data["attributes"]["risk-level"]: reportDict[data["attributes"]["risk-level"]] + 1 })
    
    return reportDict

def processCloudformationFile(ccApiKey, filePath):

    f = open(filePath, 'r')
    fileString = f.read()
    f.close()

    response = None

    if filePath.split(".")[-1].lower() == "json":
        cfJsonDict = json.loads(fileString)
        if "AWSTemplateFormatVersion" in cfJsonDict:
            response = postConformityApi(ccApiKey, str(fileString))
    else:
        if "AWSTemplateFormatVersion" in fileString:
            response = postConformityApi(ccApiKey, str(fileString))

    for severity in response:
        ux.print(ux.bold(str(severity) + " => " + str(response[severity])))

def main():
    
    supportedFileExtensions = ["json", "yaml", "yml"]

    ccApiKey = prompt.secret(
        name="CC_API_KEY",
        message="Please provide the Cloud One Conformity API Token you want to use?",
        flag="k"
    )    

    ux.spinner_start(text="Processing...")    

    filePath = None
    for (dirpath, dirnames, filenames) in walk('/ops'):       
        sdk.log(str(dirnames))
        sdk.log(str(filenames))
        status = stat(filenames[0])
        sdk.log(str(status))
        sdk.log("File permission mask (in octal):" + str(oct(status.st_mode)[-3:]))
        break

    for (dirpath, dirnames, filenames) in walk('/ops/cloudformation'):        
        sdk.log(str(filenames))
        filePath = dirpath + "/" + filenames[0]
        sdk.log(filePath)
        status = stat(filePath)
        sdk.log("File permission mask (in octal):" + str(oct(status.st_mode)[-3:]))
        break
    
    if ccApiKey != "" and filePath.split(".")[-1].lower() in supportedFileExtensions:        
        processCloudformationFile(ccApiKey, filePath)
    else:
        ux.print(str("Not a supported file. This Op only accepts json, yaml and yml files."))

    ux.spinner_stop()

    event = {
        "event_name": "conformity-pipeline-scan",
        "event_action": "succeeded"
    }
    sdk.track([], "", event)


if __name__ == "__main__":
    main()
