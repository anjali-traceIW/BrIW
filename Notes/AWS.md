# AWS

## EC2 Concepts

**Images** - what is being used to build an instance e.g. a windows image

**Instances** - the machine you're creating

**Security** - groups, key management, network interfaces

### Instance types

`<letter><number>.<size>`

Letter: type of the instance. Examples below

t: gen purpose, burstable. Unsustainable for constant large traffic load. Can do a little (hence burstable); temporary increase in capacity, then traffic will be throttled. Not production worthy

m: larger gnereal purpose instance; can sustain production level traffic. 4-500 requests per second.

Number: generation. Latest is greatest. (3)

Size: nano, micro, small, medium, large, xlarge, ... , 64xlarge. Summary of the amount of resources available, e.g. memory, storage, CPU.

download your private key and stick it in .ssh

will need to change permissions on your provate key file using `chmod 400 <private key file>` (400 gives just read permissions). Doesn't like having too open permissions on the private key.

`ssh -i <private key file> <ec2-user>@<instance ip>`

`sudo yum update`

`scp -i path/to/key (-r) file(or dir)/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/file`

## More EC2

Elastic block store - high performance, highly available storage for EC2

Load balancers - distributing traffic to a number of instances

Auto scaling - scaling the number of (base) instances of your launch coniguration

S3

Cloudfront

