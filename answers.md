# How long did you spend on the coding test below?
I spent about 2 weeks on the coding Test

# What was the most useful feature that was added to the latest version of your chosen language?
My chosen language for the frontend is Javascript, and one of the latest features added to the language is the arrow sqyntax used for declaring anonymous functions.

#  Please include a snippet of code that shows how you've used it.
I used the arrow syntax as the callback function for my axios requests.
    axios.get('https://britecore-backend-flask.herokuapp.com/category/all', { withCredentials: true })
        .then(res => this.categories = res.data)
        .catch(err => console.log(err))

# How would you track down a performance issue in production? Have you ever had to do this?
With a service called Sentry, I can configure my application send error log information via email or slack and make appropriate fixes.