# DNS-URL-Shortener
This is my project for a simple and unconventional URL shortener. I use DNS TXT records as my database instead of a traditional one. My application works by resolving a subdomain via DNS to find the destination URL that I have stored in a TXT record.

## How It Work

1.  **URL Mapping**: I map a short URL path, like `abc`, to a full subdomain, like `abc.angelasanchez.es`.
2.  **DNS Storage**: For that subdomain, I create a `TXT` record in my DNS settings. The value of this record holds the full, long URL where I want to redirect users.
3.  **Redirection Service**: I built a lightweight web application using Python and Flask. This app receives the requests for my short URLs.
4.  **DNS Lookup**: When my application gets a request, it performs a DNS query to find the `TXT` record associated with the requested subdomain.
5.  **HTTP Redirect**: If my app finds the `TXT` record, it pulls the long URL from it and sends an HTTP 302 redirect response to the user's browser, which takes them to the final destination.

## Setup

1.  **DNS Configuration**: First, I add `TXT` records for each short link I want to create in my domain's DNS management panel.
    -   **Type**: TXT
    -   **Name**: `abc`
    -   **Value**: `https://example.com/full-page`

2.  **Application**:
    -   Clone the repository.
    -   Install dependencies: `pip install -r requirements.txt`
    -   Update the `MY_DOMAIN` variable in `app.py` with my domain name.
    -   Run the Flask application: `flask --app app run`
