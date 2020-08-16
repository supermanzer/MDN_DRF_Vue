# Mozilla Developer Network - Django Rest Framework - Vue.js

Whenever I am trying to learn a new element of web development in my full-stack journey, I like to have a well defined and not-too-trick project to base it on. For me, the Mozilla Developer Network [Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) was the best help in getting me to really understand the Django web framework. Because of this, I like to revisit it regularly as I try out different approaches to building web applications. In addition to learning new things each time I review it, I find it helps me to have a set project with clearly defined goals that are broken out into easily completed steps. For this repository I will be attempting to apply the following adjustments to the original tutorial project:

- Create/Use custom User object for Authentication/Authorization
- Use [Django REST Framework](https://www.django-rest-framework.org/) to expose a REST API rather than use built in templates
- Create a simple [Nuxt.jsj](https://nuxtjs.org/) SPA front end to consume the REST API
- Utilize [Vuetify](https://vuetifyjs.com/en/) to build out UI components

## Motivation

First off, I really enjoy building different web applications and so far Django and Vue represent my favorite server and front-end frameworks. I've used Django REST Framework previously but only as a back-end developer working with a separate front-end developer.

I find the process of building every component in an application that is comprised of isolated back and front ends very illuminating in terms pf the impacts of design decisions. While this little project is pretty basic, the simplicity provides a situation where you can clearly understand how features you implement at the database level impact the user experience you can create in the front-end. Going from the quesiton "I want to display `X` to my users" to "What is the most efficient method to return calculated property `X` from the server" really helps me think through the process of building these apps beyond just trying to expose a feature to get some developer to leave you alone.

## Update - 7/5/2020

It seems I may have still bitten off a bit more than I can chew, at least in short easy segments, with the whole DRF Vue thing. My biggest issue seems to be around making the cross site request forgery protections and authentication features play nice together. I still want to understand this but it would take me farther down a rabbit hole that, for now, I don't want to go. With that in mind I've spun off a separate branch `drf_vue` which contains my as yet uncompleted attempt at making Django REST Framework and Vue work together. I will get back to this but for now I will take the incremental approach of using Vue in my Django templates. While I am most excited about building `vue-cli` projects, I want to spend more time understanding Vue itself and dealing with all of these pesky backend <=> frontend issues is distracting me. My template focused work will be in the `dj_tempalte_vue` branch

## Update 8/16/2020

Using the template approach is just too limited. Decided to go all in on fully de-coupled front and back ends. Using NuxtJS and nuxt/auth to simplify the caching and utilization of Token based authentication with my backend. Currently using DRF built-in Token authentication (unique token per user) but also interested in understanding and using JWT.

## Organization - DRF_VUE project

- backend/ - This is the Django project (wtih DRF) built by following the MDN Django tutorial (except making REST API endpoints instead of views/templates)
- frontend/ - This is the Vue.js SPA that will consume the backend server and render an interface for library patrons (staff use Django admin site)

## Vue Front End

I am _really_ basic in my Vue abilities at present so don't get your hopes up but I'm happy to be able to start quickly building out basic components that do the job I expect of them. I'm sure I'll start wanting a more cool and seamless UX that will spur greater development in that direction (I hope). For the time being, I'm just excited to get my list of books rendering like so:
![Book List](./imgs/booklist.png)

### Potential Bonus Goal - Async Django Server

I'm not really sure how to do this or what the best way to implement it is (since it's pretty brand new) but since the current version of Django (3.0.7 at the time of this writing) includes support for both synchronous (WSGI) and asynchronous (ASGI) server processes, this might be a useful project in which to attempt to implement them. We should not let a single thread in a single core of our CPU sit idle when there are requests to process!

However, the documentation on this aspect is pretty thin, both on how to implement it and why you would want to, so I don't know if I'll get to it in this project.
