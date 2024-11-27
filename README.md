# 🏆 Laddering Unite - statistical patterns & insights

What Pokemon should I team with? Should I carry solo or support the defence?

The goal of this project is to explore and analyze the underlying mechanisms behind the generative model used in Pokémon Go to determine Pokémon spawns.
The project focuses on investigating how real-world factors, such as weather and location, influence the spawning of Pokémon, as well as the relationships between the attributes of Pokémon and their spawning patterns.  

## 🚀 Get started

`report.pdf` may be your starting point to see if this project is suitable for you

Two environment are needed:

- A python one from `requirements.txt`, for data cleaning.
- A RProject one, to re-run statistical models.

## 📊 Dataset

The dataset consists of 300,000 observations collected worldwide during August 2016. Each observation includes:  

- **Pokémon ID**: A unique identifier for the spawned Pokémon (nominal variable with 150 possible values).  
- **Geolocation**: Latitude and longitude coordinates indicating where the Pokémon spawned.
- **Local Timestamp**: The time and date of the spawn event.  

Using these primary variables, additional derived variables were created to enrich the analysis:  

- **Weather conditions**.  
- **Day/night cycle** and seasonal changes.  
- **Proximity to specific geographical features** (e.g., rivers, lakes).  
- **Urban vs. rural context**.  

## 🔧 Models families

1. **Principal Component Analysis (PCA)**  

    - **Objective**: Reduce the dimensionality of Pokémon features and simplify multivariate analysis.  
    - **Findings**: Two and three components were tested, but the results were inconclusive due to low explained variance (Kaiser criterion not met).  

2. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**  

    - **Objective**: Group Pokémon based on their attributes and identify outliers.  
    - **Findings**: Clusters were not homogeneous, and the noise cluster was excessively large, even with adjustments to the radius (epsilon) parameter.  

3. **Logistic Regression (Bootstrapped)**  

    - **Objective**: Link specific real-world variables (e.g., proximity to water) to the spawn frequency of Pokémon types.  
    - **Findings**: Demonstrated that certain Pokémon types, such as water-related Pokémon, are more likely to spawn near water-related venues.

4. **Multiple Correspondence Analysis (MCA)**
   - **Objective**: Analyze and visualize relationships between nominal categorical variables.
   - **Outcome**: Helped to identify patterns and correlations between different nominal features, such as the tendency of fire Pokémon to spawn during cold nights in rural areas.

5. **Canonical Correlation Analysis (CCA)**
   - **Objective**: Explore relationships between two sets of continuous variables.
   - **Outcome**: Despite concerns about the normality of distances, CCA revealed interesting correlations, such as the spawning of fire Pokémon in colder temperatures.
