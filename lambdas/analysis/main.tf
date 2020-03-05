provider "aws" {
  region                  = "us-east-1"
  shared_credentials_file = "~/.aws/credentials"
  profile                 = "default"
}

data "archive_file" "lambda_zip" {
    type        = "zip"
    source_dir  = "${path.module}/code"
    output_path = "analysis.zip"
}

resource "aws_lambda_function" "CoordinatesValidation" {
  function_name    = "CoordinatesValidation"
  handler          = "lambda_function.lambda_handler"
  runtime          = "python2.7"
  filename         = "${data.archive_file.lambda_zip.output_path}"
  source_code_hash = "${data.archive_file.lambda_zip.output_sha}"
  role             = "arn:aws:iam::550390811644:role/LambdaBasicExecuteRole"
  memory_size      = "128"
  timeout          = "10"
}
