# Contributing to LoraComm

## Commit Convention
This project follows the [Convetional Commit guidelines](https://www.conventionalcommits.org/), which determines the following general commit format:

```
<type>(optional-scope): <description>

[optional body]
```

Optional scopes shouldn't be used often, as they clutter the commit messages. The line length of the optional body should be restricted to 80 characters, it being possible naturally to use multiple lines. The allowed keywords for types in this project are:

- `build`: Changes that affect the build system
- `chore`: Chores such as changing scripts, gitignore, etc 
- `docs`: Documentation changes
- `feat`: A new feature
- `fix`: A bug or build fix
- `perf`: Performance improvements
- `refactor`: A change that neither fixes a bug nor adds a feature
- `revert`: Undos to committed changes
- `test`: Adding missing tests or correcting existing ones

An example of a commit for this repository would be: `feat: create antenna interface`.

## Branch Naming Convention
The name of the branches in the repository should follow the format `<type>/<branch-name>`. Much like the commit convention, only a set of keywords are allowed for the branch type:

- `chore`: Chores such updating the documentation, upgrading a lib version etc
- `feat`: A new feature
- `fix`: A bug fix

The name of the branch should be written in `kebab-case`, with lowercase letters. An example of branch name for this repository would be: `fix/deadlock-reader-thread`.