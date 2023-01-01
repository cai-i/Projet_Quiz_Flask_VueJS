import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import QuestionsPage from '../views/QuestionsManager.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/start-new-quiz-page',
      name: 'quiz',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/NewQuizPage.vue')
    },
    {
      path: '/questions',
      name: 'questions',
      component: QuestionsPage
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/Admin/Admin.vue')
    },
    {
      path: '/admin/edit',
      name: 'aminEdit',
      component: () => import('../views/Admin/QuestionEdition.vue')
    },
    {
      path: '/admin/list',
      name: 'aminList',
      component: () => import('../views/Admin/QuestionList.vue')
    }

  ]
})

export default router
