package com.nitin.iiitskart;

public class Login_class {
    private String username;
    private String password;

    Login_class(String username,String password)
    {

        setUsername(username);
        setPassword(password);
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public String getUsername() {
        return username;
    }
}
