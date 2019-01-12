# Log_Analysis

## Project Overview
This is an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

## This project answers the following three questions:
1. The most popular three articles of all time.
2. The most popular authors of all time.
3. The day on which more than 1% of requests lead to errors.

## views Made
1. article_views
`create view article_views as select articles.author, articles.title, count(*) as views from articles join log on log.path like concat('%',articles.slug) group by articles.author, articles.title order by views desc;`

2. errors_view
`create view errors_view as  select dates,round( (100.0*error)/total,3) as error_percent from(select date(time) as dates, sum(case when status='200 OK' then 0 else 1 end) as error ,count(*) as total from log group by date(time)) as result order by error_percent desc;`




## How to Run?

### PreRequisites
1.[python3](https://www.python.org/downloads/)
2.[vagrant](https://www.vagrantup.com/)
3.[virtualBox](https://www.virtualbox.org/)

### Clone the Repository to your local computer using command:
`git clone  https://github.com/PRIYANSUPULAK/Log_Analysis.git`

### Start the virtual machine
From your terminal, inside the project directory, run the command 'vagrant up'. This will cause Vagrant to download the Linux operating system and install it. When downloading is finished, you will get your shell prompt back. At this point, you can run 'vagrant ssh' to log in to your newly installed Linux VM.

### Data
You can Download data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
Put the downloaded file(newsdata.sql) in the vagrant folder and unzip or extract it there.

### Loading the data
1. cd into your vagrant folder
2. Run the command
  `psql -d news -f newsdata.sql`

#### The database includes three tables:
    The **authors** table includes information about the authors of articles.
    The **articles** table includes the articles themselves.
    The **log** table includes one entry for each time a user has accessed the site.

### Make views.
Make the above mentioned views using the given commands.

### Run the program
`python3 log.py`
