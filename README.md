# Cloud One Conformity Pipeline Scanner Op

This GitHub repo is a CTO.ai Op for the [Trend Micro Cloud One Conformity](https://www.trendmicro.com/en_ca/business/products/hybrid-cloud/cloud-one-conformity.html) Pipeline Template Scanner.

The Op reads a CloudFormation template from the `/tmp/cloudformation` directory of the Op container and pushes the template contents for a **vulnerability and security misconfiguration assessment** against Cloud One Conformity rules and checks via [Conformity APIs](https://cloudone.trendmicro.com/docs/conformity/api-reference/).


> The file is validated for supported file formats (`json`, `yaml`, or `yml`) and if the file is an AWS CloudFormation template.

The Cloud One Conformity response lists all failures in the CloudFormation template by their level of severity.

> The supported Cloud One Conformity severity levels are `EXTREME`, `VERY_HIGH`, `HIGH`, `MEDIUM` and `LOW`

### Pre-requisites
---

An AWS CloudFormation template to validate AWS resource configuration for best practices and security misconfiguration. The file needs to be placed in the `cloudformation` folder of this repository.

### Required fields

 - #### **CC_API_KEY** (Conformity API Key)
        
An API key is required to authenticate requests to the Template Scanner API. You can create an API Key to access Cloud One Conformity APIs by following Conformity documentation provided here - https://www.cloudconformity.com/help/public-api/api-keys.html.
        
> For more information on Cloud One Conformity APIs, please refer to the API reference documentation available here - https://cloudone.trendmicro.com/docs/conformity/api-reference/

### Sample CloudFormation Template
---

The `sample_cloudformation_template.json` file is provided in the cloudformation folder is a sample file that you can use to test this Op. The file deploys misconfigured resources and any use of this file is your own responsibility.


## How to deploy
---

- The Op is available on the CTO.ai Ops registry [here](https://cto.ai/registry/gdcrocx/cloud-one-conformity-pipeline-scanner)

- To run the Op, you could run any of the following methods
    - run `ops run @gdcrocx/cloud-one-conformity-pipeline-scanner` on the Ops CLI
    - run `/ops run @gdcrocx/cloud-one-conformity-pipeline-scanner` on the Slack channel connected with [CTO.ai Slack App ](https://slack.com/apps/A49L9N70F-ctoai?tab=more_info)


### Related Projects

| GitHub Repository Name  | Description |
| ------------- | ------------- |
| [ConformityTemplateScanner-AWS-CodeCommit](https://github.com/GeorgeDavis-TM/ConformityTemplateScanner-AWS-CodeCommit) | Similar to this repository but catered to AWS CodeCommit repositories |
| [cloudOneConformityTemplateScanner](https://github.com/GeorgeDavis-TM/cloudOneConformityTemplateScanner) | Similar to this repository but catered to GitHub repositories |


## Contributing

If you encounter a bug or think of a useful feature, or find something confusing in the docs, please
**[Create a New Issue](https://github.com/gdcrocx/cloud-one-conformity-op/issues/new)**

 **PS.: Make sure to use the [Issue Template](https://github.com/gdcrocx/cloud-one-conformity-op/tree/master/.github/ISSUE_TEMPLATE)**

I :heart: pull requests. If you'd like to fix a bug or contribute to a feature or simply correct a typo, please feel free to do so.

If you're thinking of adding a new feature, consider opening an issue first to discuss it to ensure it aligns to the direction of the project (and potentially save yourself some time!).