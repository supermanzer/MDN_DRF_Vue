/**
 * Global application filters
 * 
 * This file registers global value filters to be used in Vue templates.  I will likely create many of my favorites 
 * from the Django template environmentbundleRenderer.renderToString
 */

import Vue from "vue"

Vue.filter("truncate", (value, numChars) => value.substring(0, numChars))
Vue.filter("truncateWords", (value, numWords) => value.split(' ').slice(0, numWords).join(' '))
Vue.filter("happyDate", (value) => {
    if (value) {
        const months = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        const dateParts = value.split('-');
        return `${months[parseInt(dateParts[1]) - 1]} ${dateParts[2]}, ${dateParts[0]}`
    } else {
        return ''
    }

})