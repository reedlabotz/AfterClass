# After Class: Bringing Social to Massive Open Online Courses

Reed La Botz  
University of Illinois at Urbana-Champaign  
https://github.com/reedlabotz/AfterClass

Massive Open Online Courses (MOOCs) have gained huge popularity over the last year with enrollments in a single class reaching as high as 160,000[^1]. Several different services have arisen that facilitate these online courses, however all fail to fully address one large aspect of an education--the need for social interactions amongst the students. Interactions amongst students help lead to a sense of community, a necessity for learning. *After Class* is a service that assists students in finding peers enrolled in a MOOC that share common goals and backgrounds to socialize with via online anonymous chat, with encouragement to move on to video or other multi-media chat when all parties are comfortable.

## Background

Massive Open Online Courses are only the latest incarnation of free, open public education, taking advantage of the power of the internet to deliver educational content to audiences around the world.

### History of Open Education

Distance learning has been attempted through several different media in the past century, first on the radio where 202 educational institutions received broadcasting licenses between 1918 and 1946. During this time one for-credit course was broadcast that failed to attract any students. In the 1970's and 1980's cable and satellite television was used to deliver educational content. In fall of 1991, eighteen institutions use the Mind Extension University Educational Network to deliver video courses[^2]. In Britain the Open University was establish in 1969 offering open enrollment to most of its courses which were broadcast by the BBC and distributed on CDs and DVDs[^3].

MOOCs are the latest version of free open education, using the power of the internet to deliver content to students. An early MOOC precursor was iTunes U which used the popular iTunes software to provide recordings of courses taught at Universities or other educational institutions to users free of charge. This system currently has over 350,000 videos in its library from a wide variety of institutions. Another system that uses the internet to present educational videos to students is the Khan Academy, offering 3500 micro lectures directed primarily at grade school children. The primary difference between the Khan Academy and other MOOCs is that the content is not separated into separate courses but instead each micro lecture is meant to stand on its own. 

### What Defines a MOOC?

All Massive Open Online Courses share two important common traits, they must have open access, meaning not only free, but also without limitations on location or organizational affiliation, and they must be scalable, meaning they can easily accommodate tens or hundreds of thousands of users [^4]. These traits often also lead to content being highly structured, and the courses relying heavily on a strong community of students to ask and answer questions in the online forums or Q&A systems. This also limits the formats of assignments that can be given in the courses, mostly machine gradeable, either multiple choice questions or code that the computer can process.

Three separate services began offering MOOCs in 2012 starting with the extremely popular course by Sebastian Thrun and Peter Norvig with an enrollment of 160,000 students[^4]. The first two websites, Udacity and Coursera, began offering courses in April 2012 and currently have one million and 750,000 members respectively. One key difference in the two sites is that Udacity courses are taught by people as individuals, while Coursera courses are offered as part of a partnership with universities. A third similar website, edX, opened registration in Fall 2012 as a partnership between MIT and Harvard with participation from several other Universities to offer MOOCs. 

Discussions of the impact that MOOCs will have on education and educational institutions have appeared repeatedly in the New York Times[^1][^5][^6], all concluding that the "lower-tier colleges, already facing resistance over high tuition may have trouble convincing students that their courses are worth the price"[^5]. The Chronicle of Higher Education speculates about the future of MOOCs and their impact on the "credit monopoly" held by educational institutions, "Someone scoring in the top 1 percent of students in a course bought by a world-famous scholar and endorsed by a world-famous university deserves no credit, while some slacker freshman who ekes out a C deserves four credits?"[^7]. The Economist questions the value of a traditional university education with soaring tuition prices, predicting that "universities will come under pressure to move to something more like a "buffet" arrangement, under which they will accept credits from each other--and from students who take courses at home"[^8].

MOOCs began in technical areas, but their popularity quickly has lead to them spreading to many different areas of study including statistics, chemistry, and poetry. These non-technical topics presented extra challenges, such as written homework responses that cannot be graded by machine and discussions that required student participation. These courses have introduced a crowd-sourcing approach which uses the students in the class as graders of each others' homework and adopted new types of multi-person video conferencing such as Google Hangouts to allow more meaningful student participation in discussions.

## Existing Solutions

All three popular MOOC systems have incorporated into their design some system for allowing students to interact amongst themselves and with course staff. Both Udacity and Coursera have Q&A style forums that allow students to ask questions and vote on the best answer. This system is perfect for factual questions, but limits the amount of discussion that can be had amongst students. For some of the discussion based courses in the humanities, Coursera has set up live webcasts of panel discussions on topics several times throughout the course. These discussions are moderated and often allow students to either submit questions electronically or wait in a queue to have a chance to join the webcast. 

Coursera has additionally teamed up with the website MeetUp which allows students to organize in-person meet-ups with groups in cities across the world. This system does allow for some face-to-face social interaction, but the MeetUp site only has a group for Coursera students, not individual courses, leaving students on their own to find a group that will share similar interests. Moreover these meeting are to occur in person limiting the availability only to those living in larger cities.

## Motivation

Social interaction plays a large role in the on campus educational system. The most important discussions often happen outside of class in hallways, dorm rooms, and coffee shops while the best learning happens in while working in study groups and on group projects. Similar interactions will play an important role in online courses as their popularity grows, giving students a sense of community, a chance to form meaningful study groups and groups for projects. One aspect of social interaction that becomes especially important in online courses is the community that it offers, allowing students to realize they are not alone in the class. This provides students an outlet to discuss problems they may have in the course. In a traditional setting it has been argued that "students with poor interpersonal relations are more likely to experience academic failure" and that community may be essential to "meaningful, deep learning"[^9]. 

## My Approach

*After Class* takes a data-centric approach to helping users find group mates. The forums offered by MOOC providers have no structured data and leave students to search through thread subject lines for students that will share common goals. *After Class* collects user data through a series of surveys which ask questions aimed at helping users find define their goals in taking the course. 

### Design

*After Class* is designed to give users the maximum amount of useful information about their potential group mates without overwhelming them with abundant questions and provide a fun and friendly interface for finding partners. The website is organized around several key activities that the user needs to complete:

* Sign up and create authentication credentials
* Enter basic demographic and personal information
* Add courses
* Explore the roster of other students
* Interact with groups they have formed

The visual design of the website is meant to be simple, only introducing bright colors for the buttons that move users from one section to the next. The name and logo are chosen to reflect a school environment, but to also suggest that this is not a part of the class and that discussions within these groups not always be limited to course material.

![After Class Logo](https://raw.github.com/reedlabotz/AfterClass/master/app/static/img/logo.png)

As there is lots of initial information that must be collected from the users upon their sign up, the welcome screens needed to be simple and un-intimidating. Each of the sections of the opening questionnaire is accompanied by a short explanation of why that information will be helpful.

### Process

The core of this service is its ability to provide users with data about potential partners that will lead to partner choices with the most chance of success. Choosing which questions to ask is a delicate decision that must balance the utility of the data gained against the potential to exhaust the user with too many questions. 

Olson and Olson define two relevant concepts important to having groups that work well together[^10]. The first is common ground, "knowledge that the participants have in common, and that they are aware they have in common."[^10] The second is collaboration readiness which consists of two dimensions, work-related and social. The work-related dimension is that "the goals of the subgroups need to be aligned" while the social dimension is that "there is some benefit for all participants"[^11]. The questions chosen are directed at satisfying these collaboration requirements. 

The first interaction that users have is purely text based and remains pseudo-anonymous giving only the answers to survey questions as identifying information, but to have the most productive interactions users should be urged to use a multi media chatting system. Video chat was shown to improve remote interaction by allowing users to "express understand or agreement, forecast responses, enhance verbal descriptions, give purely nonverbal information, express attitudes through posture and facial expression, and manage extended pauses"[^12].

### Goals

The goal of this system is to assist users in finding groups that will be beneficial to the their experience in a course. The proper pairing for each person may vary widely, so *After Class* avoids an algorithmic approach to finding partners and instead opt to provide an organized set of data on each user that will allow users to choose partners they think will work well with them. 

### Final Design and Implementation

*After Class* is created using the Django Python web application framework.

#### Getting User Information

To sign up for the service users are asked to give a username and password for future login. The first welcome screen that users see asks for basic personal and demographic information. This information will allow students to better filter potential study-buddies based on who they believe they will work best with. Users are asked the following questions in this section:

* What is your age? (10-19, 20-29, 30-39, 40-49, 50-59, 60-69,70-79, 80+)
* What is your gender? (Male, Female, Other)
* Which best describes you? (Highschool Student, Undergraduate Student, Graduate Student, Academic, Professional, Other)
* Which learning style best describes you? (Visual, Auditory, Tactile) 
* What is your area of interest? (Agriculture, Anthropology, Archeology, etc.)
* Tell us a little about yourself, (140 characters remaining)

These questions are aimed at deciding if the users have common ground meaning they have similar backgrounds and education levels.

![Personal and demographic information screen](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/welcome-step-1.png)

One of the great features of a MOOC is the flexibility it offers to fit in to busy schedules and allow students from anywhere in the world to take the course, this does however mean that students enrolled in the same class might have drastically different schedules. To account for this students are also asked to select times when they are generally available from a week calendar. During the group finding process students are immediately informed if another student shares one or more available blocks in common.
 
![Availability screen](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/welcome-step-2.png)

Once students have completed the personal information and availability surveys they are asked to add all of the massive online courses they are enrolled in. When adding each course they are asked about their background and reasons for taking the course. I ask both about their experience in the general area of study and the specific topic to better understand their level with the material of the course. All questions are phrased in such a way that they can apply to any area of study that might be available through one of the online course providers. For each course the following questions are asked: 

* What is your level for this course's general area of study? (Novice, Intermediate, Advanced)
* What is your level for this course's specific topic? (Novice, Intermediate, Advanced)
* How many years of experience do you have in this area? (<1 year, 1-2 years, 2-5 years, >5 years)
* Why are you taking this course? (Interest in new topic, Refresher on topic, Background for a new class, Recommended by a friend/teacher, Taking with a friend, Required for a different course, Other)
* Are you taking this course for credit at any academic institution? (Yes, No)
* What is your primary goal from taking this course? (Get a new job, Gain experience in this topic, Curiosity about a topic, Other)

These questions add to the discovery of common ground, but mainly hit on collaboration readiness, making sure that both students have similar goals including the goal of receiving credit or not.  

![Add course screen](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/add-course.png)

#### Helping Users Find Groups

The most important aspect of this service is the ability for students to find other students that will be good partners for them. To help in this process I show users a graph in the explore section that shows how similar to themselves other students are. This allows students to look for other students that they think will be a good fit or them, be it someone who is very similar or someone who is a polar opposite. This visualization represents the current user as a large black circle surrounded by other users represented by the smaller colorful dots. The distance of each dot from the user represents the number of similar responses from the survey. As users hover over a users detail box, that users circle on the visualization is highlighted, and inversely if the user mouses over a dot in the visualization, the user profile represented by that dot is scrolled into view.

![Explore screen](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/explore.png)

One a user sends a partner request the requested user is notified and asked to accept or reject the request based on the same user information provided in the explore screen. During the request process the personal information of neither party is given to the other until both have approved the group.

![Requests notice](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/request.png)

![Request screen](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/partner-request.png)

#### Interacting with a Group

The core of the system is the chat interface which allows users to get to know each other in a very low pressure environment. Once users have accepted each other into a group, they are permitted to now see first names to allow them to identify themselves. This is still an anonymous chat that allows them to interact without knowing any specifics about the person they are chatting with. The meta information about each user is shown to give an ice breaker and allow the users to remember details about the user they are talking to.

![Chat interface](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/chat.png)

After the group members have had a chance to get to know each other in an anonymous setting, each user is asked if they feel comfortable having a video chat with their partner, and once both partners agree, a video chat is suggested and potential times from their schedule are suggested.

![Video suggestion](https://raw.github.com/reedlabotz/AfterClass/master/writing/screenshots/video_interest.png)

### Future Features

Although the main focus of this project is to find groups for online interaction, the same system could also assist students to find groups for in person meet-ups. This has the benefit over the current solution offered by MOOC providers of having all the meta data about students in the class allowing people to only join meet-ups which will be productive.

### Critique

One primary failure of the current implementation is that users are limited to only the set of answers that are repopulated for each of the questions in the survey. While a write-in could be provided for users that feel that none of the options sufficiently describe them, this would limit the ability of the software to properly determine the similarities of users. This may cause the sorting of similarity to be incorrect because many users choose the "other" choice. If a more advanced similarity algorithm that used keyword extraction or natural language processing were used then users could be allowed to enter their own text where only select boxes are currently offered.

The system that is created here still forces users to manually look through each of the students in the roster to determine if they would be a good match, which will not scale well to courses with tens of thousands of students. Although filtering could be employed to narrow down the results, a more automated pairing process would likely be more successful for extremely large courses.

## Future Research

The next step in this project will be to get a field trial with real students. To be able to test the efficacy of the system in finding productive groups students would need to be asked an extra survey about their previous experience in MOOCs as well as surveys about how much they enjoy the meetings they have with their groups, and if the groups added to their enjoyment or learning in the course.

Since groups are made up of students with a shared enrollment in a class, advertising for only one or two courses will allow students to find groups and will ensure that there is a good number of students to explore through for each of the targeted classes.

[^1]: Richard Pérez-Peña. "Top Universities Test the Online Appeal of Free." New York Times 17 July 2012. 10 December 2012 <http://www.nytimes.com/2012/07/18/education/top-universities-test-the-online-appeal-of-free.html> 

[^2]: Nasseh, Bizhan. "A brief history of distance education." Adult Education in the News (1997).

[^3]: "Open University." Wikipedia: The Free Encyclopedia. Wikimedia Foundation, Inc. 7 December 2012. Web. 10 December 2012.

[^4]: "Massive Open Online Course." Wikipedia: The Free Encyclopedia. Wikimedia Foundation, Inc. 9 December 2012. Web. 10 December 2012.

[^5]: Tamar Lewin. "College of Future Could Be Come One, Come All." New York Times 19 November 2012. 10 December 2012 <http://www.nytimes.com/2012/11/20/education/colleges-turn-to-crowd-sourcing-courses.html?pagewanted=all>.

[^6]: Tamar Lewin. "A Class Where Opening Minds, Not Earning Credits, Is the Point." New York Times 19 November 2012. 10 December 2012 <http://www.nytimes.com/2012/11/20/education/online-course-opens-minds-to-world-music.html>.

[^7]: Kevin Carey. "Into the Future with MOOC's." The Chronicle of Higher Education 3 September 2. 10 December 2012 <http://chronicle.com/article/Into-the-Future-With-MOOCs/134080/>.

[^8]: "Higher education: Not what it used to be." The Economist 10 December 2012 <http://www.economist.com/news/united-states/21567373-american-universities-represent-declining-value-money-their-students-not-what-it>.

[^9]: Rovai, Alfred P. "A preliminary look at the structural differences of higher education classroom communities in traditional and ALN courses." Journal of Asynchronous Learning Networks 6.1 (2002): 41-56.

[^10]: Olson, Gary M., and Judith S. Olson. "Distance matters." Human-computer interaction 15.2 (2000): 139-178.

[^11]: Olson, Judith S. et al. "A Theory of Remote Scientific Collaboration." _Scientific collaboration on the Internet_. Cambridge, Mass: MIT Press, 2008. 

[^12]: Ellen A. Isaacs and John C. Tang. 1993. "What video can and can't do for collaboration: a case study." In Proceedings of the first ACM international conference on Multimedia (MULTIMEDIA '93). ACM, New York, NY, USA, 199-206. DOI=10.1145/166266.166289 <http://doi.acm.org/10.1145/166266.166289>

