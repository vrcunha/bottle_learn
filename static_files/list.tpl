<html>
    <head>
        <title>Listing</title>
    </head>
    <body>
        % include('static_files/menu')
        <p>Table Products:</p>
            <table border="1">
                <tr>
                    <td>ID</td><td>Name</td><td>Price</td><td>stock</td>
            </tr>
            %for row in rows:
            <tr>
            %for col in row:
                <td>{{col}}</td>
            %end
            </tr>
            %end
</table>
    </body>
</html>