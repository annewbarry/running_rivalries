## Abstract: 
In this project I explored the idea of whether middle aged men and young women perform similarly in running races.  By scraping results data from the New York Road Runners website for the 2019 New York City Marathon and 2019 5th Avenue Mile, I used a Z-test to compare the mean times for Women ages 30-34 to those of men in age groups 40-49, 50-54, 55-59, and 60-64, finding that the mean time for men was faster except in the case of the 60-64 age group.


## Background and Motivation

New York Road Runners holds around two dozen races annually in New York City, serving runners of all ages across distances from 200 meters all the way to the marathon.  I participated in dozens of races with them over the course of 7 years and I observed time and time again: the people nearest to me while I raced always seemed to be populated mostly by other competitive women in their 20s and 30s and men in their mid 40s.  My training partners often were middle-aged men and I began to wonder if in general young women were closely matched with men in their 40s. This hypyothesis seemed interesting to pursure, as at some point one would think that a man's advancing age begins to outweigh the advantages of his biological sex, when compared to younger women.  I also was interested in seeing how relatively competitive the groups were based on the distance of the race, either a mile or a marathon, because the mile race favors youth, whereas many people don't people in the marathon until their 30s or later.

This study also appealed to me because one reason I love running is how it brings people together in unexpected ways, across age, sex, and background, because at the end of the day, all that matters is how fast you are.  There's something beautiful to the idea that for all our differences in experiences, my best running buddy might be a man 15 or more years older than me (in fact, some already were; I learned a lot about fatherhood on my long runs!).

## Research Question, Data, and a Refined Research Question

*Question*: Do young women run as fast as middle-aged men in road races?

*The Data* My big question of gender parity had to be narrowed so that I could conduct my research in a manageable way.  I used the race results for the 2019 New York City Marathon and the 2019 5th Avenue Mile from the New York Road Runners website.  The data included the name, age, gender, and finish time of each person.  I was able to select age groups in 5 year increments: Women 25-29, Women 30-34, Men 40-44, Men 45-49, Men 50-54, Men 55-59, Men 60-64.  Because my initial observation was based on my experience seeing many men in their 40s, I primarily focused on comparing the Men 40-44 and Men 45-49 to the women.  Using these two races as my samples, I hoped to make conclusions about the population of New York Road Runners race participants in general, regardless of year or distance.


*Refined Research Question*: Are the mean New York Road Runners race times the same for Women runners ages 25-34 and Men runners ages 40-49? 

## The Process

*Data Journey*: To obtain the data, I used Selenium to scrape the race results from NYRR.org, parsed the HTML through BeautifulSoup, and then stored the results in a MongoDB container.  Then, I moved all of the data to a Pandas Dataframe.

*Refinement*: I removed all race times that were slower than an average of 12 minutes per mile, as that is by some standards the cutoff for what is considered running instead of jogging.  The heart of my big picture question seeks to compared he average capabilities of these two demographics, so I wanted to filter the data even further, keeping only people who are competitive, meaning someone who keeps trying to run their best race, regardless of how fast they are.  I made a new dataframe that included only runners who ran both races, thinking that a person who did more than one race in a year would be more serious about pushing themselves to run their best.
