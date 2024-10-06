<%
String uname = request.getParameter("username");  // Retrieve the username from the form input
Cookie ck = new Cookie("username", uname);        // Create a new cookie with the name "username" and value as the user's input
ck.setMaxAge(1 * 60);                             // Set the cookie's maximum age to 60 seconds (1 minute)
response.addCookie(ck);                           // Add the cookie to the response, which sends it to the browser
%>
<html>
<body>
   <h3>Cookie Saved</h3>
   <p><a href="showcookie.jsp">View the cookie value</a></p>
</body>
</html>
