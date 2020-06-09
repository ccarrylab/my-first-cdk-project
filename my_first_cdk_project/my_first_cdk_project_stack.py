from aws_cdk import(
 aws_s3 as _s3, 
 aws_iam as _iam,
 core
)


class MyFirstCdkProjectStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        
        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="myfirstcdkproject021",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
        )

        mybucket = _s3.Bucket(
         self,
         "myBucketId1"
        )

        snstopicname="abcxyz1234"

        if not core.Token.is_unresolved(snstopicname) and len(snstopicname) > 10:
            raise ValueError("Maximum value can be only 10 characters")

        print(mybucket.bucket_name)

        _iam.Group(self,
                    "gid")
     
        output1 = core.CfnOutput(
            self,
            "myBucketOutput1",
            value=mybucket.bucket_name,
            description=f"My first CDK Bucket",
            export_name="myBucketOutput1"
     )