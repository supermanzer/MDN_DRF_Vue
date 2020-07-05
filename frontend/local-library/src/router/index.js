import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [{
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import( /* webpackChunkName: "about" */ "@/views/About.vue")
  },
  {
    path: "/books",
    name: "Books",
    props: true,
    component: () => import('@/views/Books.vue'),
    children: [{
      path: ':id',
      name: 'Book',
      props: true,
      component: () => import( /* webpackChunkName: "book"*/ '@/components/Books/BookDetail.vue'),
    }]
  },
  {
    path: '/authors',
    name: 'Authors',
    component: () => import('@/views/Authors.vue'),
    children: [{
      path: ':id',
      name: 'Author',
      props: true,
      component: () => import( /* webpackChunkName: "author" */ '@/components/Authors/AuthorDetail.vue')
    }]
  },
  {
    path: '/genres',
    name: 'Genres',
    component: () => import('@/views/Genres.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import( /* webpackChunkName: "login" */ '@/views/Login.vue')
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;