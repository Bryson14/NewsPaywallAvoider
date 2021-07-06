# News Paywall Avoider

Have you ever gone to sites like TechnologyReview.com, nytimes.com, or others as seen at this [site](https://www.reddit.com/r/worldnews/wiki/paywalls)? Well its annoying because many times it loads the page but quickly stops the reader from seeing anything. Well this quick and dirty python script tries to skirt around this by pulling the raw html sent from the server, not rendering the JS, and printing out all the paragraph elements contents.

* Bascially, if the contents are there but then the JavaScript keeps your from scrolling, then this script might help. If the information is not sent from the server, well then sorry, you're out of luck. *

- wsj.com and kyivpost.com always returns a 403 Forbidden error. The times doesn't render the entire page out. The raw response from the server only includes the first paragraph so its almost useless.

## Its not perfect, but it might get the job done
- Run by calling `python news_paywall_avoider.py URL`
