<!DOCTYPE HTML>
<html lang="en">
    <head>
        <title>IT Terminology</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
        <link rel="stylesheet" href="the.css">
        <script src="jquery-2.1.3.min.js"></script>
        <script src="the.js"></script>
        <template id="spinner">
            <div class="spinner">
        	    <div class="spinner-container container1">
        	    	<div class="circle1"></div>
        	    	<div class="circle2"></div>
        	   	<div class="circle3"></div>
        	    	<div class="circle4"></div>
        	    </div>
        	    <div class="spinner-container container2">
        	    	<div class="circle1"></div>
        	    	<div class="circle2"></div>
        	    	<div class="circle3"></div>
        	    	<div class="circle4"></div>
        	    </div>
        	    <div class="spinner-container container3">
        	    	<div class="circle1"></div>
        	    	<div class="circle2"></div>
        	    	<div class="circle3"></div>
        	    	<div class="circle4"></div>
        	    </div>
        	</div>
        </template>
        <template id="entry">
            <div class="entry">
                <div class="title">{0}</div>
                <article>{1}</article>
                <div class="catagory">{2}</div>
            </div>
        </template>
    </head>
    <body>
        <header>
            IT Terminology
        </header>
        <nav>
            <div class="title">
                Add Entry
            </div>
            <form action="/" method="POST">
                <input type="text" name="title" placeholder="Title">
                <input type="text" name="catagory" placeholder="Catagory">
                <textarea rows="10" cols="60" name="description" placeholder="Description"></textarea>
                <input value="Add Entry" type="submit">
            </form>
            <script>
                $('nav').click(function() {
                    $('nav').addClass('up');
                });
            </script>
        </nav>
        <section>
            U Have JS boi??
        </section>
    </body>
</html>
