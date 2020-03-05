# CoordinatesValidation

![badge](https://img.shields.io/badge/version-1.0.0-green.svg)

> A solution to validate coordinates.

Request
``` json
{
  "latitude": -76.2313,
  "longitude": 187.013
}
```

Response with a boolean if the coordinates are valid
``` json
{
  "valid": true
}
```

## Table of Contents

- [Requirements](#requirements)
- [Install](#install)
- [Tests](#tests)

## Requirements
- Install [Python](https://www.python.org/downloads/)
- Install [Git](https://git-scm.com/downloads)
- Install [Terraform](https://www.terraform.io/downloads.html)
- Install [AWS CLI](https://docs.aws.amazon.com/es_es/cli/latest/userguide/installing.html)

## Install
### Get repository:
``` bash
$ git clone git@github.com:JoValo/realEstate.git
$ cd lambdas/analysis
```

### Configure AWS CLI
``` bash
$ aws configure
```
AWS CLI ask for credentials, example
``` bash
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: json
```

### Create infrastructure in AWS with Terraform
Open the `main.tf` file with your favorite editor and:
1. In the `provider` declaration change the `shared_credentials_file` attribute by the path of your AWS credentials `Users/yourusername/.aws/credentials`.
2. If you have more than one profile you must change also `profile` attribute and set your profile name.

Then:
``` bash
$ cd ..
$ terraform init
$ terraform plan
```
If everything is ok.
```bash
$ terraform apply -auto-approve
```

When finish you can destroy this infrastructure with next command (only in sandbox environment):
```bash
$ terraform destroy
```

#### References
- [Longitude](https://en.wikipedia.org/wiki/Longitude#Noting_and_calculating_longitude)
- [Latitude](https://en.wikipedia.org/wiki/Latitude#The_graticule_on_the_sphere)
