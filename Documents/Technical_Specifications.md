# Technical Specifications

<details>
<summary> Table of contents </summary>

- [Technical Specifications](#technical-specifications)
      - [Teams Members](#teams-members)
      - [Reviewers](#reviewers)
    - [What/When/Why](#whatwhenwhy)
    - [Background](#background)
    - [Goals](#goals)
    - [Non-Goals](#non-goals)
    - [Plan](#plan)
    - [Measuring Impact](#measuring-impact)
    - [Security, Privacy, Risks](#security-privacy-risks)
    - [Other Considerations](#other-considerations)
    - [Milestones](#milestones)
    - [Open Questions](#open-questions)
</details>

#### Teams Members

|Members|Roles |
|:---:|:---:|
|[Nicolas Mida](https://github.com/Nicolas-Mida)| Project Manager|
|[Clément Caton](https://github.com/ClementCaton)| Tech Leader|
|[Théo Trouvé](https://github.com/TheoTr)| Team Member|
|[Salaheddine Namir](https://github.com/T3rryc)| Team Member|
|[Victor Leroy](https://github.com/Victor-Leroy)| Team Member|
|[Alexandre Bobis](https://github.com/AlexandreBobis)| Team Member|

#### Reviewers

  - [Franck Jeannin](https://github.com/frje)

  - [Jackie Boscher](https://github.com/ia35)

### What/When/Why

This project needs to be done in 9 weeks , the objective is to create a device that can detect the language people are speaking. In Algosups case, we are mainly focused on French and English, to avoid students who are speaking French during class or project time.

### Background

One of the main objective of Algosup is to make students speaking English while they are in class, the more you speak the more you will learn. The idea is to make students speak English during their breaks, the lunch time and also the more important during the project time. So the idea came up. How to make them speak only in English during their project time without having to come in their room each hour ?

### Goals

The goal of this project is to create a device, which is able to detect if the people around are speaking French or English, and be able to warn the user around if they speak in the wrong language. In our case, we need to speak only in English

### Non-Goals

We cancelled the idea of using an Arduino device , due to a lack of storage on the Arduino device, which was not enough for us to be able to do an efficient model with the free space on it.

### Plan
 - Week 1

During the first week, our objectives will be to write the documents, find information about artificial intelligence and how we will succeed in this project.

 - Weeks 2 and 3

Then, we will take 2 weeks to find databases that we can use and also find the best format we will need.

 - Weeks 4, 5 and 6

For weeks 4, 5 and 6, we will look for the best solutions to process the data, the type of data we will use to form future data and which will be the best for our utility.

 - Weeks 7 and 8

During weeks 7 and 8, we will be at the point where we will have to find the best possible model and also configure the device to be able to use the model and thus detect the voice.

 - Week 9

Over the last week, we will take the time to prepare the presentation and, depending on the progress of the project, we may be able to change some things that do not work.

### Measuring Impact

### Security, Privacy, Risks

- The first risk, is that the accuracy of the model will be too low and the device won't work well.
- The second risk is a low memory capacity of the device. That's why we use Raspberry PI.

- For the privacy, the audio file will be transformed into an image, we store the image while it is replaced by the next one. The sentences will therefore only be stored for a short time.

### Other Considerations
### Milestones
### Open Questions
