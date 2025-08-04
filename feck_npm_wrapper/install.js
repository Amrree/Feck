const { execSync } = require('child_process');

console.log('Installing feck (Python package) via pip...');

try {
  // Install the Python package using pip
  execSync('pip install thefeck --user', { stdio: 'inherit' });

  // Set up aliases (this part is tricky for npm, usually done in shell config)
  console.log('\nFeck (Python) installed. Please add the following to your shell config (e.g., ~/.bashrc, ~/.zshrc):');
  console.log('eval $(thefeck --alias)');
  console.log('eval $(thefeck --alias FECK)');
  console.log('eval $(thefeck --alias OHFECK)');
  console.log('eval $(thefeck --alias OHFECKIT)');
  console.log('eval $(thefeck --alias BATFECK)');
  console.log('eval $(thefeck --alias CURLFECK)');
  console.log('\nRemember to source your shell config file after adding these aliases.\n');

} catch (error) {
  console.error('Failed to install feck (Python package):', error.message);
  process.exit(1);
}
