#Readme

##Curriculum Ticket Dashboard

The Curriculum Ticket Dashboard is an MVP for support tickets. Ticket data is sourced from an internal Confluence spreadsheet. Ticket data is organized by key views. The dashboard is setup for both executive view and ticket support view. This MVP will be developed further to create an internal PowerBI Dashboard.

##Motivation

Curriculum Ticket Data was unactionable for both executive and resolution teams. A v1 PowerBI Dashboard was in use but did not include key views. With knowledge of Python I built a v2 dashboard. This dashboard is for demoing key views (as expressed by leadership) and functionality required (as determined by SMEs).

##Build Status: Complete

  - [√] Create class to wrap pandas + plotly
  - [√] Plot Piechart of errors by category
  - [√] Plot Funnel of errors by course
  - [√] Plot Barchart of time to resolve errors by course
  - [√] Create Dashboard
  - [√] Deploy via Flask

##Screencast

(CurricDashboardVid)


##Libraries Used

Model: Pandas, Plotly
View: Dash, Flask
Controller: N/A