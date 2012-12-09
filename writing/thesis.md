# After Class: Bringing Social to Massive Open Online Courses

Reed La Botz  
University of Illinois at Urbana-Champaign  
https://github.com/reedlabotz/AfterClass

Massive Open Online Courses (MOOCs) have gained huge popularity over the last year with enrollments in a single class reaching as high as 160,000[^1]. Several different services have arisen that facilitate these online courses, however all fail to fully address one large aspect of an education -- the need for social interactions amongst the students. After Class is a service that assists students in finding peers enrolled in a MOOC that share common goals and backgrounds to socialize with via online anonymous chat, with encouragement to move on to video or other multi-media chat when all parties are comfortable.

## Background

Massive Open Online Courses are only the latest incarnation of free, open public education, taking advantage of the power of the internet to deliver educational content to audiences around the world.

### History of Open Education

BBC and PBS and radio education.

MOOCs are also not the first version of free education that use the power of the internet to deliver content to students. One of the earliest MOOC precursors was iTunes U which used the popular iTunes software to provide recordings of courses taught at Universities or other educational institutions to users free of charge. This system currently has over 350,000 videos in its library from a wide variety of institutions. Another system that uses the internet to present educational videos to students is the Khan Academy, offering 3500 micro lectures directed primarily at grade school children. The primary difference between the Khan Academy and other MOOCs is that the content is not separated into separate courses but instead each micro lecture is meant to stand on its own. 

### What Defines a MOOC?

All Massive Open Online Courses share two important common traits, they must have open access, meaning not only free, but also without limitations on location or organizational affiliation, and they must be scalable, meaning they can easily accommodate tens or hundreds of thousands of users [^2]. These traits often also lead to content being highly structured, and the courses relying heavily on a strong community of students to ask and answer questions in the online forums or Q&A systems. This also limits the formats of assignments that can be given in the courses. Most courses try to stick to homework that is machine gradeable, either multiple choice questions or code that the computer can process.

2012 has been the year of the MOOC with  three different websites have beginning to offer MOOCs. The first two websites, Udacity and Coursera, began offering courses in April 2012 and now have one million and 750,000 members respectively. One key difference in the two sites is that Udacity courses are taught by people as individuals, while Coursera courses are offered as part of a partnership with universities. A third similar website, edX, has opened registration in Fall 2012 as a partnership between MIT and Harvard with participation from several other Universities to offer MOOCs. 

Discussions of the impact that MOOCs will have on education and educational institutions have appeared repeatedly in the New York Times[^3][^4][^5], all concluding that "lower-tier colleges, already facing resistance over high tuition may have trouble convincing students that their courses are worth the price" [^3]. The Chronicle of Higher Education speculates about the future of MOOCs and their impact on the "credit monopoly" held by educational institutions, "Someone scoring in the top 1 percent of students in a course bought by a world-famous scholar and endorsed by a world-famous university deserves no credit, while some slacker freshman who ekes out a C deserves four credits?"[^6]. The Economist questions the value of a traditional university education with soaring tuition prices, predicting that " universities will come under pressure to move to something more like a "buffet" arrangement, under which they will accept credits from each other--and from students who take courses at home"[^7].

MOOCs began in technical areas, but their popularity quickly has lead to them spreading to many different areas of study including statistics, chemistry,  and poetry. These non-technical topics presented extra challenges, such as written homework responses that couldn't be graded by machine and discussions that required student participation. These courses have introduced a crowd sourcing approach to use the students in the class as graders of each others homework and adopted new types of multi-person video conferencing such as Google Hangouts to allow more meaningful student participation in discussions.

## Existing Solutions

All three current MOOC systems have incorporated into their design some system for allowing students to interact amongst themselves or with course staff. Both Udacity and Coursera have Q&A style forums that allow students to ask questions and vote on the best answer. This system is perfect for factual questions, but limits the amount of discussion that can be had amongst students. For some of the discussion based courses in the humanities, Coursera has set up live webcasts of panel discussions on topics several times throughout the course. These discussions are moderated and often allow students to either submit questions electronically or wait in a queue to have a chance to join the webcast. 

Coursera has additionally teamed up with the website MeetUp which allows students to organize in-person meet-ups with groups in cities across the world. This system does allow for some face-to-face social interaction, but the MeetUp site only has a group for Coursera students, not individual courses, leaving students on their own to find a group that will share similar interests. Moreover these meeting are to occur in person limiting the availability only to those living in larger cities.

## Motivation

Social interaction plays a large role in the current on campus educational system. The most important discussion happen outside of class in hallways, dorm rooms, and coffee shops while the best learning happens in working in study groups and on group projects. Similar interactions will play an important role in online courses as their popularity grows, giving students a sense of community, a chance to form meaningful study groups and groups for projects. One aspect of social interaction that becomes especially important in online courses is the sense of community that it offers, allowing students to realize they are not alone in the class and have an outlet to discuss problems or lack of understanding with other students. 

## My Approach

After Class takes a data-centric approach to helping users find group mates. The current forums offered by MOOC providers have no structured data and leave students to search through thread subject lines for students that will share common goals. After Class collects user data through a series of surveys which ask questions aimed at helping users find define their goals in taking the course. 

### Design

After Class is designed to give users the maximum amount of useful information about their potential group mates without overwhelming them with abundant questions and provide a fun and friendly interface for finding partners. The website is organized around several key activities that the user needs to complete:

* Sign up and create authentication credentials
* Enter basic demographic and personal information
* Add courses
* Explore the roster of other students
* Interact with groups they have formed

The visual design of the website is meant to be simple, only introducing bright colors for the buttons that move users from one section to the next. The name and logo are chosen to reflect a school environment, but to also suggest that this is not a part of the class and that discussions within these groups not always be limited to course material.

![After Class Logo](https://raw.github.com/reedlabotz/AfterClass/master/app/static/img/logo.png)

As there is lots of initial information that must be collected from the users upon their sign up, the welcome screens needed to be simple and un-intimidating. Each of the sections of the opening questionnaire is accompanied by a short explanation of why that information will be helpful.

### Process



### Goals

### Final Design

#### Getting User Information

After completing the basic sign up for the website, users are asked to complete a first section of the survey asking basic personal and demographic information. This information will allow students to better filter potential study-buddies based on who they believe they will work best with. Users are also asked for a tweet length bio to give some more information to potential group-mates.

![Personal and demographic information screen](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/welcome-step-1.png)

One of the great features of a MOOC is the flexibility it offers to fit in to busy schedules and allow students from anywhere in the world to take the course, this does however mean that students enrolled in the same class might have drastically different schedules. To account for this students are also asked to select times when they are generally available from a week calendar. During the group finding process students are immediately informed if another student shares one or more available blocks in common.
 
![Availability screen](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/welcome-step-2.png)

Once students have completed the personal information and availability surveys they are asked to add all of the massive online courses they are enrolled in. When adding each course they are asked about their background and reasons for taking the course. We ask both about their experience in the general area of study and the specific topic to better understand their level with the material of the course. All questions are phrased in such a way that they can apply to any area of study that might be available through on of the online course providers. 

![Add course screen](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/add-course.png)

#### Helping Users Find Groups

The most important aspect of this service is the ability for students to find other students that will be good partners for them. To help in this process we show users a graph in the explore section that shows how similar to themselves other students are. This allows students to look for other students that they think will be a good fit or them, be it someone who is very similar or someone who is a polar opposite.

![Explore screen](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/explore.png)

One a user sends a partner request the requested user is notified and asked to accept or reject the request based on the same user information provided in the explore screen. During the request process the personal information of neither party is given to the other until both have approved the group.

![Requests notice](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/request.png)

![Request screen](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/partner-request.png)

#### Interacting with a Group

The core of the system is the chat interface which allows users to get to know each other in a very low pressure environment. Once users have accepted each other into a group, they are permitted to now see first names to allow them to identify themselves. This is still an anonymous version of chat that allows them to interact without knowing any specifics about the person they are chatting with. We continue to display the meta information about each user to give a sort of ice breaker and allow the users to remember some more information about the user they are talking to.

![Chat interface](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/chat.png)

After the group members have had a chance to get to know each other in an anonymous setting, each user is asked if they feel comfortable having a video chat with their partner, and once both partners agree, a video chat is suggested and potential times from their schedule are suggested.

!TODO: Add video suggest screenshot

### Implementation

After Class is created using the Django Python web application framework. 

### Future Features

Although the main focus of this project is to find groups for online interaction, the same system could also assist students to find groups for in person meet-ups. This has the benefit over the current solution offered by MOOC providers of having all the meta data about students in the class allowing people to only join meet-ups which will be productive.

### Critique

## Future Research

The next step in this project will be to get a field trial with real students. To be able to test the efficacy of the system in finding productive groups students would need to be asked an extra survey about their previous experience in MOOCs as well as surveys about how much they enjoy the meetings they have with their groups, and if the groups added to their enjoyment or learning in the course.

Since groups are made up of students with a shared enrollment in a class, advertising for only one or two courses will allow students to find groups and will ensure that there is a good number of students to explore through for each of the targeted classes.


[^1]: http://www.nytimes.com/2012/07/18/education/top-universities-test-the-online-appeal-of-free.html

[^2]: http://en.wikipedia.org/wiki/Massive_open_online_course

[^3]: "College of Future Could Be Come One, Come All"

[^4]: "Top Universities Test the Online Appeal of Free"

[^5]: "A Class Where Opening Minds, Not Earning Credits, Is the Point"

[^6]: "Into the Future with MOOC's"

[^7]: "Higher education: Not what it used to be"