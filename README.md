# CompareWebPageContent
Comparing Wev Page Content

Transporting with hierarchy, with different attr(our attr)
Like this:
```
      <html>
          <head></head>
          <body>
              <ul class="asd">
                  <li class="qwe">
                      <p>
                          <h2>
                              <a href="/show/">Hey</a>
                          </h2>
                          <h2></h2>
                      </p>
                  </li>
                  <li></li>
              </ul>
          </body>
      </html>
      # We are added different attr all tag, and just keep in mongodb example: # Like Unix System
      { 'tag':'html'} # Normally
      { 'tag':'html', 'hierarchy':'/html'} # We are used this.
      { 'tag':'head', 'hierarchy':'/html/head'}
      { 'tag':'body', 'hierarchy':'/html/body'}
      { 'tag':'ul'  , 'class':'asd', 'hierarchy':'/html/body/ul[asd]'}
      { 'tag':'li'  , 'class':'qwe', 'hierarchy':'/html/body/ul[asd]/li[qwe]'}
      { 'tag':'p'   , 'hierarchy':'/html/body/ul[asd]/li[qwe]/p'}
      { 'tag':'h2'  , 'hierarchy':'/html/body/ul[asd]/li[qwe]/p/h2'}
      { 'tag':'a'   , 'href':'/show', 'hierarchy':'/html/body/ul[asd]/li[qwe]/p/h2/a'}
      { 'tag':'h2'  , 'hierarchy':'/html/body/ul[asd]/li[qwe]/p/h2'}
      { 'tag':'li'  , 'class':'qwe', 'hierarchy':'/html/body/ul[asd]/li'}
```

<h4>How does it look on MongoDb</h4>

![MongoDb](https://github.com/pleycpl/CompareWebPageContent/blob/master/picture/RoboMongoDisplay.png)

<h4>Xpath-Nice-Document</h4>
<ul>
  <li>http://www.pearsonitcertification.com/articles/article.aspx?p=101369&seqNum=3</li>
  <li>http://www.w3schools.com/xml/xpath_intro.asp</li>
  <li>https://msdn.microsoft.com/en-us/library/ms256086(v=vs.110).aspx</li>
</ul>
