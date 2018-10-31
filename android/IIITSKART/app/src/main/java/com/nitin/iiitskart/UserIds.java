package com.nitin.iiitskart;

public class UserIds {
    private String User;
    private String Concat;
    private String last_msg;
    public UserIds(String User,String Concat,String last_msg){
        setConcat(Concat);
        setUser(User);
        setLast_msg(last_msg);
    }

    public UserIds(){

    }

    public void setLast_msg(String last_msg) {
        this.last_msg = last_msg;
    }

    public void setUser(String user) {
        this.User = user;
    }

    public void setConcat(String concat) {
        this.Concat = concat;
    }

    public String getUser() {
        return User;
    }

    public String getConcat() {
        return Concat;
    }

    public String getLast_msg() {
        return last_msg;
    }
}
