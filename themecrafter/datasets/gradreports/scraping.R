# Script for scraping data from gradreports.com

# Required libraries
library(xml2)
library(stringr)
library(tidyverse)

# Base url of the website
baseurl <- "https://www.gradreports.com"

# First, we gather a list of links of the reviews pages for each school

## The list of schools is broken up into different pages.
## We run through the pages extracting the table rows and concatenate them.
page_id <- 1
schools <- list()

nrows <-  1
while (nrows > 0) {
    # Page url
    schools_url <- paste0(baseurl, "/colleges?page=", page_id)
    print(schools_url)
    
    schools_on_page <- read_html(schools_url, options = c("NOERROR", "NOBLANKS") ) %>% 
        xml_find_one(xpath='//div[@class="table_school_list"]') %>% 
        xml_find_all(xpath='//tbody//tr')
    
    schools <- c(schools, schools_on_page)
    
    # Check number of schools
    nrows <- length(schools_on_page)
    print(nrows)
    
    page_id <- page_id + 1
}


## Now we have a list of schools from which we can extract the links 
college_name_cell <- schools %>% map(xml_find_one, xpath='td[1]') %>% map(xml_children)
recommendation_cell <- schools %>% map(xml_find_one, xpath='td[2]//a')
nreviews_cell <- schools %>% map(xml_find_one, xpath='td[3]//a')

school_name <- college_name_cell %>% map_chr(xml_text)
school_reviews_page <- college_name_cell %>% map_chr(xml_attr, attr='href')
school_recommendation <- recommendation_cell %>% map_chr(xml_text)
school_nreviews <- nreviews_cell %>% map_chr(xml_text)

## We can put all this in a data frame
school_df <- data.frame(name=school_name,
                        reviews_page = school_reviews_page,
                        recommendation = school_recommendation,
                        nreviews = school_nreviews)

## We can then tidy the data frame
school_df %>% 
    mutate_all(str_trim)


# Now, we obtain a list of links to the reviews pages for each school
reviews_links <- school_df %>% 
    mutate(reviews_page = str_c(baseurl, reviews_page)) %>% 
    pull(reviews_page)


for (i in 1:length(reviews_links)){
    # link to the first reviews page
    baselink <- reviews_links[i]
    
    page_id <- 1
    reviews <- list()
    
    nreviews <-  1
    while (nreviews > 0) {
        # Page url
        review_url <- paste0(baselink, "?page=", page_id)
        print(review_url)
        
        reviews_on_page <- read_html(review_url, options = c("NOERROR", "NOBLANKS") ) %>% 
            xml_find_one(xpath='//div[@id="review-list"]') %>% 
            xml_find_all(xpath='//div[@class="review panel"]')
        
        reviews <- c(reviews, reviews_on_page)
        
        # Check number of schools
        nreviews <- length(reviews_on_page)
        print(nreviews)
        
        page_id <- page_id + 1
    }
}


## All the information needed is stored in the list of review-panel nodes
url2 <- "https://www.gradreports.com/colleges?page=2"

# Obtain a data frame of the first pages to search

url <- "https://www.gradreports.com/colleges/indiana-university-purdue-university-indianapolis?page=2"

r <- read_xml(url, as_html = TRUE, options = c("NOBLANKS", "NOERROR") ) %>% 
    html_node(xpath='//div[@id="review-list"]') %>% 
    html_nodes(xpath='//div[@class="review panel"]')

r <- r %>% html_text()
