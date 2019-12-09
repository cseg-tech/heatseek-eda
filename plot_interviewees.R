# libraries
library(ggplot2)
library(lubridate)

# load data
heatseek = read_csv("data/heatseek_geocoded.csv")
interviewees = filter(heatseek, user_id %in% c(446, 381, 509, 447, 441, 391)) %>%
  mutate(user_id = as.factor(user_id))

# split into separate df for users
interviewees_list = split(interviewees, interviewees$user_id)
user_names = list("446" = "Pedro Soler",
                  "381" = "Corine Ombongo",
                  "509" = "Dorothy Romain",
                  "447" = "Liz Bieber",
                  "441" = "Gibson Mitchel",
                  "391" = "Allen Delin")

# create plots
for (i in interviewees_list) {
  df <- i %>%
    mutate(date = date(created_at)) %>%
    group_by(user_id, date) %>%
    summarise(mean_temp = mean(temp))
  
  user <- user_names[as.character(unique(df$user_id))]
  
  plot <- ggplot(df, aes(x = date, y = mean_temp)) +
    geom_line() +
    geom_hline(aes(yintercept = 68, linetype = "Day (68F)"), color = "red") +
    geom_hline(aes(yintercept = 62, linetype = "Night (62F)"), color = "blue") +
    labs(x = "Date",
         y = "Average Daily Temperature",
         title = paste("Average Daily Temperatures for", user)) +
    scale_linetype_manual(name = "Threshold", values = c(2, 2),
                          guide = guide_legend(override.aes = list(color = c("red", "blue")))) +
    scale_x_date(date_breaks = "1 month", date_labels = "%b")
    theme_bw()
  
  print(plot)
}