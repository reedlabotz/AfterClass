var page = new WebPage()

page.onConsoleMessage = function(msg) {
   if(msg == "exit()"){
      phantom.exit();
   }else{
      console.log(msg);
   }
};

page.open('https://www.coursera.org/courses', function (status) {
    if (status !== 'success') {
        output.errors.push('Unable to access network');
    } else {
        page.evaluate(function(){
            function waitOver(){
               var courses = [];
               var cells = jQuery('.coursera-course-listing-box');
               for(var i=0;i<cells.length;i++){
                  var course = {};
                  course['name'] = jQuery(cells[i]).find(".coursera-course-listing-name a").html();
                  course['url'] = "https://www.coursera.org" + jQuery(cells[i]).find(".coursera-course-listing-name a").attr('href');
                  course['professor'] = jQuery(cells[i]).find(".coursera-course-listing-instructor").html();
                  course['service'] = 'c';
                  course
                  courses.push(course);
               }
               console.log(JSON.stringify(courses));
               console.log("exit()");
            }

            jQuery(document).ready(function(){
               setTimeout(waitOver,3000);
            });
        });
    }
});

