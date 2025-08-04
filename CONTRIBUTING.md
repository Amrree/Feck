# Contributing to `feck`: Let's Make Mistakes Better, Together (and Have a Laugh!)

Welcome, fellow human, to the `feck` contribution guide! We believe that making mistakes is part of the journey, and fixing them should be a delightful experience. If you're here, it means you're ready to join our quest to make the command line a friendlier, more forgiving, and perhaps even a bit more hilarious place. So, let's get fecking started!

## Reporting Issues: Found a Blunder? Tell Us (No, Really!)!

Even `feck` isn't perfect (gasp!). If you stumble upon a bug, a typo that `feck` missed, or a command it should have corrected but didn't, please let us know! Your keen eye helps us all, and who knows, your bug might even inspire a new, wonderfully silly rule.

Before you open an issue, please:

1.  **Update `feck`**: Run `pip install thefeck --upgrade` to ensure you're on the latest version. Maybe we've already fixed it (or introduced an even funnier one!).
2.  **Check Existing Issues**: Your bug might already be reported. Give the issue tracker a quick search. Don't be afraid to add your own witty comments if it's relevant!

If it's still there (oh, feck!), open a new issue on our [GitHub Issues page](https://github.com/Amrree/Feck/issues) and include:

*   The output of `thefeck --version` (e.g., `feck 3.x using Python 3.x.x`).
*   Your shell and its version (Bash, Zsh, Fish, PowerShell, etc.).
*   Your operating system (Linux distribution, macOS version, Windows version, Termux version, etc.).
*   Clear steps to reproduce the bug (the command you typed, the error it gave, and what `feck` did or didn't do). Feel free to describe the level of your frustration in vivid detail!
*   The output of `thefeck` with `THEFUCK_DEBUG=true` exported (run `export THEFUCK_DEBUG=true` in your shell before trying `feck`). This helps us see the inner workings, even if they're a bit messy.
*   If it's application-specific, the application's output and version.
*   Any other juicy, hilarious, or utterly baffling details you think might help us squash that bug!

## Making a Pull Request: Share Your Fecking Brilliance (and Your Shenanigans)!

We absolutely adore pull requests! Whether you've crafted a brilliant new rule, polished an existing one, added a snazzy feature, or simply fixed a typo in our documentation (ironic, isn't it?), your contributions are celebrated. We especially encourage contributions that add a touch of humor, silliness, or a nod to the absurdities of life (and the command line).

Here's a general workflow for contributing code:

1.  **Fork the Repository**: Head over to [https://github.com/Amrree/Feck](https://github.com/Amrree/Feck) and click the "Fork" button. It's like cloning, but with more personal flair!
2.  **Clone Your Fork**: `git clone git@github.com:YourUsername/Feck.git`
3.  **Create a New Branch**: `git checkout -b feature/your-awesome-feature` or `fix/your-bug-fix` (or `shenanigans/my-hilarious-addition` - we won't judge!)
4.  **Make Your Changes**: Write your code, create new rules (the funnier, the better!), improve documentation, etc. Don't be afraid to get creative!
5.  **Test Your Changes**: Run `pytest` to ensure everything is still working as expected. If you add new rules, please add tests for them! We need to make sure our jokes land properly.
6.  **Commit Your Changes**: Write clear, concise, and perhaps even witty commit messages. Let your personality shine!
7.  **Push to Your Fork**: `git push origin feature/your-awesome-feature`
8.  **Open a Pull Request**: Go to your fork on GitHub and open a pull request to the `main` branch of the original `Amrree/Feck` repository. Tell us about your changes, and don't forget to mention any particularly amusing moments during development!

We'll review your pull request, provide feedback, and work with you to get your changes merged! We're always looking for ways to make `feck` even more delightful.

## Developing Locally: Get Your Hands Dirty (and Maybe a Bit of Tea!)

Want to hack on `feck` on your local machine? Fantastic! We support a couple of development setups:

### Using a Local Python Installation

1.  **Create and activate a Python 3 virtual environment.** (Highly recommended! It's like a cozy little cottage for your code.)
2.  **Install `feck` for development:**
    ```bash
    pip install -e . --user
    ```
    (Make sure you are in the root of the `feck` repository, e.g., `/data/data/com.termux/files/home/feck_temp`)

3.  **Run code style checks:**
    ```bash
    flake8
    ```

4.  **Run unit tests:**
    ```bash
    pytest
    ```

5.  **Run unit and functional tests (requires Docker):**
    ```bash
    pytest --enable-functional
    ```

### Using a VSCode Dev Container

For a hassle-free setup, especially if you're new to Python development or want a consistent environment, use the provided VSCode Dev Container. It comes with all prerequisites pre-installed, so you can focus on the fun stuff.

**Prerequisites:**

*   [Docker](https://www.docker.com/products/docker-desktop)
*   [VSCode](https://code.visualstudio.com/)
*   [VSCode Remote Development Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
*   [Windows Users Only]: [WSL2 and Docker Desktop configured to use it](https://docs.docker.com/docker-for-windows/wsl/)

**Running the container:**

1.  Open VSCode.
2.  Open the Command Palette (CMD+SHIFT+P on Mac or CTRL+SHIFT+P on Windows).
3.  Select `Remote-Containers: Reopen in Container`.
4.  The container will build, install all `pip` requirements, and your VSCode will magically connect to it.
5.  Your VSCode and container now become a disposable development environment! It's like a tiny, self-contained world for your code.

## License

`feck` is open-source and distributed under the MIT License. See `LICENSE.md` for the full text.
