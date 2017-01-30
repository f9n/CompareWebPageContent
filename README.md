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
      { 'tag':'html', 'hierarchy':'/'} # We are used this.
      { 'tag':'head', 'hierarchy':'/head'}
      { 'tag':'body', 'hierarchy':'/body'}
      { 'tag':'ul', 'class':'asd', 'hierarchy':'/body/ul[asd]'}
      { 'tag':'li', 'class':'qwe', 'hierarchy':'/body/ul[asd]/li[qwe]'}
      { 'tag':'p', 'hierarchy':'/body/ul[asd]/li[qwe]/p'}
      { 'tag':'h2', 'hierarchy': '/body/ul[asd]/li[qwe]/p/h2'}
      { 'tag':'a', 'href':'/show', 'hierarchy':'/body/ul[asd]/li[qwe]/p/h2/a'}
      { 'tag':'h2', 'hierarchy': '/body/ul[asd]/li[qwe]/p/h2'}
      { 'tag':'li', 'class':'qwe', 'hierarchy':'/body/ul[asd]/li'}
```

<h4>Xpath-Nice-Document</h4>
<ul>
  <li>http://www.pearsonitcertification.com/articles/article.aspx?p=101369&seqNum=3</li>
  <li>http://www.w3schools.com/xml/xpath_intro.asp</li>
  <li>https://msdn.microsoft.com/en-us/library/ms256086(v=vs.110).aspx</li>
</ul>
