# **Memo Bubble**

## **Overview**

![Home page]()<br>

Deployed API Heroku: [API link]()

Deployed Frontend Heroku: [Memo Bubble]()

Backend Github [Repository]()

Frontend Github [Repository]()

## **Table of Contents**
* [**Overview**](#overview)
* [**User experience**](#user-experience-ux)
    + [**Strategy plane**](#strategy-plane)
        - [**Site goals**](#site-goals)
        - [**Opportunities**](#opportunities)
    + [**Scope plane**](#scope-plane)
    + [**Structure plane**](#structure-plane)
        - [**Developer Tasks & User Stories**](#developer-tasks--user-stories)
    + [**Skeleton plane**](#skeleton-plane)
        - [**Wireframes**](#wireframes)
        - [**Database schema**](#database-schema)
    + [**Surface plane**](#surface-plane)
        - [**Color Scheme**](#color-scheme)
        - [**Background image**](#background-image)
        - [**Background pattern**](#background-pattern)
        - [**Typography**](#typography)
* [**Agile Development**](#agile-development)
* [**SEO & Marketing**](#business-model-seo--marketing)
    - [**SEO**](#seo)
    - [**Marketing**](#marketing)
* [**Features & Future Development**](#features--future-development)
    - [**Features**](#features)
    - [**Future Development**](#future-development)
* [**Technologies used**](#technologies-used)
* [**Testing**](#testing)
* [**Deployment**](#deployment)
* [**Acknowledgement & Credits**](#acknowledgement--credits)
* [**Media**](#media)
    - [**Images**](#images)
* [**Conclusion**](#conclusion)

# **User experience (UX)**

During the planning phase we used 5 planes to create our design.

## **Strategy plane**

### **Site goals**

* Offer a user-friendly site to browse through.
* Implement fully functional features.
* Create a user-friendly interface with intuitive navigation.
* Create a responsive design for seamless browsing across devices.
* Implement like feature for capsules. 
* Offer ability to leave comments on capsules and read other user comments.
* Implement a notifications feature for likes and comments on user capsules.
* Implement SEO best practices to improve visibility in search engines and leverage digital marketing strategies.

### **Opportunities**

Opportunity | Importance | Viability/Feasibility
---|---|---
User register/login | 5 | 5
User profile | 5 | 5
User comments | 3 | 4
User likes | 3 | 4
Admin login | 5 | 5
Capsule searching | 5 | 5
Password recovery | 5 | 5
About page | 5 | 5
Contact form | 5 | 5
Social media links | 3 | 5
Notifications | 3 | 3
SEO implementation | 5 | 5
Privacy Policy | 3 | 3
FAQ | 2 | 2
---|---|---
Total ||

## **Scope plane**

Due to a deadline for this project as for anything in life and to avoid scope creep, we used MoSCoW method to keep project on track and concentrate on delivering fully functional site. Unfortunately, since beginning of the project we knew we won't have time to implement everything we would like so decided to leave some features for future development. During development some features might be added/ discarded and some design changes are possible. Our MoSCoW method planning can be seen below:

* Must Have:
    + Admin login
    + User register
    + User login/logout
    + Capsule list rendered as bubbles
    + Individual capsule page
    + Personal information safety
    + Add a capsule
    + Edit/update a capsule
    + Delete a capsule
    + Contact details

* Should Have:
    + Personalized profile
    + Edit/update a profile
    + Capsule search
    + Search results
    + Contact form
    + Privacy Policy

* Could Have:
    + Notifications
    + Likes
    + Leave a comment
    + Delete a comment for admin
    + Email confirmation after registration
    + Password recovery
    + FAQ

* Won't Have:
    + Subscription

## **Structure plane**

### **Developer Tasks & User Stories**

We have created tasks/ user stories and project for this app: 
* Task and user stories can be found following this link: [GitHub Issues](https://github.com/violaberg/memo-bubble/issues)
* Project can be found following this link: [Kanban Board](https://github.com/users/violaberg/projects/9).

## **Skeleton plane**

### **Wireframes**

Wireframes for both desktop and mobile were created with [Balsamiq](https://balsamiq.com/) and can be seen in wireframes folder. Please keep in mind that some changes/ additions were made during development but basis for project were designed in these wireframes:
* [Desktop wireframes]()
* [Mobile Wireframes]()

### **Database schema**

We created database schema to design the structure and organization of a database to efficiently store, manage, and retrieve data. This was crucial part when creating models and try and escape unneccesary migration complications. Original and updated database schema can be found below:

![Original database schema]()

![Updated database schema]()

## **Surface plane**

### **Color Scheme**

For this project we chose 7 colors - White `#faf9f6`, Light Cyan `#00cccc`, Lightest Blue `#d0fffe`, Dark Cyan `#009393`, Olive Dark Green `#808000`, Error Color Bright Red `#c90000` and our Primary Text Color Deep Blue `#030011`. This color palette combines the purity of white with the warmth of goldenrod and the depth of midnight blue, creating a harmonious balance of sophistication and elegance. The colors work together to highlight the beauty of gemstones and create a luxurious, visually engaging and immersive experience for users.

![Color palette]()

### **Background image**

![Image]()

### **Background pattern**

To add more depth and interest to design but not make it overwhelming for user to look at, we created a pattern for background using our White colour `#faf9f6`.<br>

![Pattern]()

### **Typography**

In planning of the visual identity of our app, we meticulously selected two Google fonts, Exo2 and Orbitron.<br>

![Exo2]()

![Orbitron]()

# **Agile Development**

We have included details of agile development in a separate file [AGILE.md](AGILE.md).

# **SEO & Marketing**

## **SEO**

SEO, or Search Engine Optimization, is the process of improving your website to increase its visibility when people search for products or services related to your business on search engines like Google. The better visibility your pages have in search results, the more likely you are to attract attention and draw prospective and existing customers to your business. All search in Google was done in incognito window.
For keyword research purposes we used [Keyword Surfer](https://surferseo.com/keyword-surfer-extension/) Chrome extension and checked search results directly in Google Tools. We have included a brain dump using keywords and Google to return a list of long and short-tail keywords. All screenshots can be found in [SEO](static/docs/seo) folder. Below we have added tables created so search results are better visible:

<details><summary>Search results</summary><img src="static/docs/seo/search-table.png"></details>
<details><summary>Search results</summary><img src="static/docs/seo/search-table2.png"></details>

After concluding our research we added descriptive meta tags to the project.

## **Marketing**

* ***Who are your users?***<br>

* ***Which online platforms would you find lots of your users?***<br>
Users can be found on social media platforms.

* ***Would your users use social media? If yes, which platforms do you think you would find them on?***<br>
Yes, users would likely be active on Instagram, Pinterest, and Facebook.

* ***What do your users need? Could you meet that need with useful content?***<br>

* ***What are the goals of your app? Which marketing strategies would offer the best ways to meet those goals?***<br>
The goals are to build a reliable platform to store and share memories, build brand awareness, and retain users. Effective marketing strategies include content marketing, social media engagement, email marketing, and possible influencer collaborations.

# **Features & Future Development**

## **Features**

* Favicon<br>

    ![Favicon]()

* Brand name<br>

    ![Brand name]()

* Logo<br>

    ![Logo]()

* Navigation<br>

    ![Navigation]()

* Likes<br>

    ![Likes]()

* Notifications<br>

    ![Notifications]()

* Sign up<br>

    ![Sign up]()

* Login<br>

    ![Login]()

* Contact form<br>

    ![Contact form]()

* FAQ page<br>

    ![FAQ page]()

* Footer<br>

    ![Footer]()

* Capsule Page<br>

    ![Gemstone card]()

* Capsules List Page (Bubbles)<br>

    ![Capsules List]()

* Profile<br>

    ![Profile]()

* Profile - Edit form<br>

    ![Profile Edit form]()

* Profile - User capsules<br>

    ![User capsules]()

* Comment<br>

    ![Comment]()

* Comment form<br>

    ![Comment form]()

## **Future Development**

In the second half of development we realized what we won't be able to implement due to dealine fast approaching.

# **Technologies used**

* HTML
* CSS
* Javascript
* Python
* Django
* Django allAuth
* Bootstrap
* [Heroku](https://www.heroku.com/)
* Jinja
* jQuery
* Whitenoise
* AWS S3 Bucket

# **Testing**

We have included details of testing in a separate file [TESTING.md](TESTING.md).

# **Acknowledgement & Credits**

* [Hero Patterns](https://heropatterns.com/) used to create background pattern
* [Google Fonts](https://fonts.google.com/) used to find and implement fonts
* [Font Awesome](https://fontawesome.com/) used for icons
* Favicon created using [Favicon Generator](https://www.favicongenerator.com/)
* Privacy Policy generated with [Privacy Policy Generator](https://www.privacypolicygenerator.info/)
* [Keyword Surfer](https://surferseo.com/keyword-surfer-extension/) used for some Google searches
* Search result table generated with [Table Generator](https://www.table-generator.de/)

# **Media**

## **Images**
* 

# **Conclusion**