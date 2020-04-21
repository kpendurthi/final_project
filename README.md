# final_project
Overview
This application allows employers to add, edit, view and delete jobs and employees to view jobs


Project Links
GitHub: (https://github.com/kpendurthi/final_project)
heroku: https://myjobrecruiterapp.herokuapp.com/

Technologies used:
Django framework , postgress database and css


MVP -
View list of jobs available to apply and list of employers who posted the jobs
Add/Edit a job and employers
update job posting
update employer details
delete jobs and employers




add authentication for users to update/edit/create/delte job and employers

User Stories
as a user(employer or employee), I can view a list of jobs 
as a user, I can add/edit a job
as a user, I can add/edit employer details and job deatils
as a user, I can delete existing jobs

Models
Table Employer

Field	        Property
Company_Name	character field
Company_Address Char Field
Email           Char Field
username        Char Field




Table job

Field	           Property
employer	        foreign key
title 	            CharField
description  	    CharField
location            CharField
type                CharField
category            CharField
last_date           CharField
company_name        CharField
company_description CharField
website             CharField
image url	        CharField
created_at          CharField
filled	            BooleanField
salary              IntegerField

   
   
   

Issues and Resolutions
Use this section to list of all major issues encountered and their resolution.


issue #2 login and authentication problem (after login it is not going showing default page)
resolution: forgot add redirecgt page setting in settings.py file. 
