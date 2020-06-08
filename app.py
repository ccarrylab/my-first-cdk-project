from aws_cdk import aws_s3 as _s3, core

from my_first_cdk_project.my_first_cdk_project_stack import MyFirstCdkProjectStack


app = core.App()
MyFirstCdkProjectStack(app, "my-first-cdk-project")

app.synth()

