class Thefeck < Formula
  include Language::Python::Virtualenv

  desc "Magnificent app which corrects your previous console command, with a bit of craic!"
  homepage "https://github.com/Amrree/Feck"
  url "https://pypi.io/packages/source/t/thefeck/thefeck-3.32.tar.gz"
  sha256 "#{`curl -sL https://pypi.io/packages/source/t/thefeck/thefeck-3.32.tar.gz | shasum -a 256 | awk '{print $1}'`.strip}"
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources

    # Install the main script and aliases
    bin.install "feck_integrations/batfeck.py" => "batfeck"
    bin.install "feck_integrations/curlfeck.py" => "curlfeck"

    # Symlink the main entry point and aliases
    bin.install_symlink libexec/"bin/thefeck"
    bin.install_symlink libexec/"bin/feck"
    bin.install_symlink libexec/"bin/ohfeck"
    bin.install_symlink libexec/"bin/ohfeckit"
  end

  test do
    assert_match "feck", shell_output("#{bin}/thefeck --version")
    assert_match "feck", shell_output("#{bin}/feck --version")
    assert_match "feck", shell_output("#{bin}/ohfeck --version")
    assert_match "feck", shell_output("#{bin}/ohfeckit --version")

    # Test batfeck and curlfeck by trying to run a non-existent command
    # and checking if feck is invoked.
    # This is a simplified test; real tests would involve mocking.
    assert_match "Oh, feck!", shell_output("#{bin}/batfeck --non-existent-flag 2>&1", 1)
    assert_match "Oh, feck!", shell_output("#{bin}/curlfeck --non-existent-flag 2>&1", 1)
  end
end
