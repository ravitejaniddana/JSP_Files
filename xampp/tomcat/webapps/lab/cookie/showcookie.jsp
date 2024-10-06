<html>
<body>
   <h3>Reading the cookies</h3>
   <%
   Cookie[] array = request.getCookies();  // Retrieve all cookies from the request
   for (int i = 0; i < array.length; i++)  // Loop through each cookie
   {
      if (array[i].getName().equals("username"))  // Check if the cookie name is "username"
      {
         out.println("<br/>");
         out.println("Name of the cookie : " + array[i].getName() + "<br/>");  // Print the cookie name
         out.println("Value in cookie : " + array[i].getValue());  // Print the cookie value (the username)
      }
   }
   %>
</body>
</html>
