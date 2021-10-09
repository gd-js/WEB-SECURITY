# Cloud based web app checklist for speed and security

## Speed

Point domain only, and only to load balancer  

Cache all slow, frequent and stable queries  

Static files HTTP caching for css, js, jpeg, png -> put on AWS S3/ Google Cloud  

Solve bottlenecks: Memory, CPU, Network I/O, Disk I/O  

Compute heavy logic offline/ Static web app HTML file  

Maintain database indexes  

CDN over subdomain/ CNAME, zip via gzip/minify  

Session data into cookies/ redis, memcached  

## Security

Keep only HTTP (80) SSL (443) ports  

Disable ssh root and passauth (/etc/ssh/sshd_config/, PermitRootLogin no, PasswordAuthentication no)  

Manage access via ssh public keys (~/.ssh/authorized_keys)  

Never serve off nginx root/ Apache DocumentRoot  

Serve user content on entirely different domain  

Always use Object Relational Mapper (ORM)  

Always use HTML template library (ORM)  

Always use CSRF Tokens  

Never open redirects  

Use crypto library to add unique salt to all user data  

Demand strong password input  

Never identify a user through cookies  
