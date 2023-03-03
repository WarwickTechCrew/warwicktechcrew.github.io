# warwicktechcrew.co.uk

The web homepage for Warwick Tech Crew.

A static HTML site generated with Jekyll by GitHub Pages.

## Updating

The content of the website is complied by Jekyll from a set of human readable YAML files in `_data/`

### Shows

Shows are stored in annual YAML files in `_data/shows/`.

You can add `notes` to a term to be displayed above the shows (see Term 3 2019/2020), as well as `links` below the roles in a show (see photo galleries in earlier years).

The standard format is below:

```yaml
year: 2012 / 2013

terms:
- name: Term 1
  notes: This was a strange term, we don't talk about it.
  shows:
  - name: "Tech Crew: The Musical"
    society: Tech Crew X MTW
    venue: Warwick Arts Centre Theatre
    people:
    - role: Tech Manager
      name: Amanda Fleming
    - role: Prime Minister
      name: Who the f*ck knows anymore
    links:
    - name: Images
      label: Happy
      url: https://unsplash.com/photos/m6BphieLlwA
```

#### Importing Script

Though I can't see any reason you'd need to use it (was initially used to migrate the old fully static website to Jekyll), the `_bin/html_to_yaml.py` can be used to scrape the show information of the HTML of the webpage.

### Exec

The exec members info is stored in `_data/exec.yaml`. You could put multiple years of exec in, the webpage (currently) will only display the top year in the file.

Exec photos located in `/assets/img/exec` **MUST** be `.jpg`. The filenames should be provided in `exec.yaml`

The main webpage template is located at /index.html
