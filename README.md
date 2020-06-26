## A web scraper in a Docker container hosted on AWS

This example illustrates how to build and run a Docker image containing Firefox web browser, Python libraries, such as Selenium and etc., to host a web scraper on AWS. 

## Instructions

The example contains a CloudFormation script to rebuild the project and infrastructure automatically on AWS. Please update `home.py` file in `code` folder with your logic. Then, archive the content of code folder while naming `code.zip` the archive and upload it to your S3 bucket, which is specified in CF script under the name `S3HostingBucket`.

## Note

The solution relies on Firefox browser, which has constant updates with important security fixes. Please make sure that you are running the latest version of it or consider alternatives. For example, Selenium requires a web browser, however other scraping libraries can run independently. 

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

