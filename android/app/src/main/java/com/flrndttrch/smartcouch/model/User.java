package com.flrndttrch.smartcouch.model;

import com.google.gson.annotations.SerializedName;

import java.math.BigInteger;

public class User {
    @SerializedName("id")
    private Integer id;
    @SerializedName("first_name")
    private String firstName;
    @SerializedName("last_name")
    private String lastName;
    @SerializedName("username")
    private String username;
//    @SerializedName("password")
//    private String password;
    @SerializedName("date_joined")
    private String dateJoined;
//    @SerializedName("email")
//    private String email;
    @SerializedName("is_active")
    private boolean isActive;
    @SerializedName("is_staff")
    private boolean isStaff;
//    @SerializedName("is_superuser")
//    private boolean isSuperuser;
    @SerializedName("last_login")
    private String lastLogin;

    public User(Integer id, String firstName, String lastName, String username, String dateJoined,
                boolean isActive, boolean isStaff, String lastLogin) {
//    public User(int id, String firstName, String lastName, String username, String password,
// String dateJoined,
//                String email, boolean isActive, boolean isStaff, boolean isSuperuser, String
// lastLogin) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.username = username;
//        this.password = password;
        this.dateJoined = dateJoined;
//        this.email = email;
        this.isActive = isActive;
        this.isStaff = isStaff;
//        this.isSuperuser = isSuperuser;
        this.lastLogin = lastLogin;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getDateJoined() {
        return dateJoined;
    }

    public void setDateJoined(String dateJoined) {
        this.dateJoined = dateJoined;
    }

    public boolean isActive() {
        return isActive;
    }

    public void setActive(boolean active) {
        isActive = active;
    }

    public boolean isStaff() {
        return isStaff;
    }

    public void setStaff(boolean staff) {
        isStaff = staff;
    }

    public String getLastLogin() {
        return lastLogin;
    }

    public void setLastLogin(String lastLogin) {
        this.lastLogin = lastLogin;
    }
}
