package com.flrndttrch.smartcouch.model;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class LightingResponse {
    @SerializedName("page")
    private int page;
    @SerializedName("objects")
    private List<Lighting> results;
    @SerializedName("total_results")
    private int totalResults;
    @SerializedName("total_pages")
    private int totalPages;

    public LightingResponse(int page, List<Lighting> results, int totalResults, int totalPages) {
        this.page = page;
        this.results = results;
        this.totalResults = totalResults;
        this.totalPages = totalPages;
    }

    public int getPage() {
        return page;
    }

    public void setPage(int page) {
        this.page = page;
    }

    public List<Lighting> getResults() {
        return results;
    }

    public void setResults(List<Lighting> results) {
        this.results = results;
    }

    public int getTotalResults() {
        return totalResults;
    }

    public void setTotalResults(int totalResults) {
        this.totalResults = totalResults;
    }

    public int getTotalPages() {
        return totalPages;
    }

    public void setTotalPages(int totalPages) {
        this.totalPages = totalPages;
    }
}
