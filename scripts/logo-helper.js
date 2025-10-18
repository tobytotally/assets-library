/**
 * Logo Helper - Utility for accessing GitHub-hosted logo assets
 *
 * Usage:
 *   getLogoUrl('crisis', 'white')
 *   → https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/crisis/crisis-white.png
 */

const LOGO_BASE_URL = 'https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/';

/**
 * Get URL for a specific logo variation
 *
 * @param {string} clientName - Client identifier (e.g., 'crisis', 'jp-morgan')
 * @param {string} variation - Logo variation: 'original', 'trimmed', 'white', 'black', 'icon-512', 'icon-1024', 'landscape', 'portrait', 'square'
 * @returns {string} Full GitHub raw URL to the logo
 *
 * @example
 * // Get original logo
 * getLogoUrl('crisis', 'original')
 *
 * @example
 * // Get white version for dark mode
 * getLogoUrl('crisis', 'white')
 *
 * @example
 * // Get social media icon
 * getLogoUrl('crisis', 'icon-512')
 */
function getLogoUrl(clientName, variation = 'original') {
  // Normalize client name
  const normalized = clientName
    .toLowerCase()
    .trim()
    .replace(/\s+/g, '-')
    .replace(/[^a-z0-9-]/g, '');

  // Validate variation
  const validVariations = [
    'original', 'trimmed', 'white', 'black',
    'icon-512', 'icon-1024',
    'landscape', 'portrait', 'square'
  ];

  if (!validVariations.includes(variation)) {
    console.warn(`Invalid variation "${variation}". Using "original". Valid options: ${validVariations.join(', ')}`);
    variation = 'original';
  }

  return `${LOGO_BASE_URL}${normalized}/${normalized}-${variation}.png`;
}

/**
 * Get all variation URLs for a client
 *
 * @param {string} clientName - Client identifier
 * @param {string} layout - Layout type: 'landscape', 'portrait', or 'square' (default: 'landscape')
 * @returns {Object} Object with all variation URLs
 *
 * @example
 * const crisisLogos = getAllLogoUrls('crisis');
 * // Returns: { original: '...', white: '...', black: '...', trimmed: '...', icon512: '...', icon1024: '...', layout: '...' }
 */
function getAllLogoUrls(clientName, layout = 'landscape') {
  const normalized = clientName.toLowerCase().trim().replace(/\s+/g, '-');

  return {
    original: getLogoUrl(clientName, 'original'),
    trimmed: getLogoUrl(clientName, 'trimmed'),
    white: getLogoUrl(clientName, 'white'),
    black: getLogoUrl(clientName, 'black'),
    icon512: getLogoUrl(clientName, 'icon-512'),
    icon1024: getLogoUrl(clientName, 'icon-1024'),
    layout: getLogoUrl(clientName, layout)
  };
}

/**
 * Create an HTML img element with responsive dark/light mode support
 *
 * @param {string} clientName - Client identifier
 * @param {string} alt - Alt text for the image
 * @param {string} cssClass - Optional CSS class name
 * @returns {string} HTML <picture> element with dark/light mode support
 *
 * @example
 * createResponsiveLogo('crisis', 'Crisis Logo', 'proposal-logo')
 * // Returns HTML with white logo for dark mode, black for light mode
 */
function createResponsiveLogo(clientName, alt, cssClass = '') {
  const whiteUrl = getLogoUrl(clientName, 'white');
  const blackUrl = getLogoUrl(clientName, 'black');
  const classAttr = cssClass ? ` class="${cssClass}"` : '';

  return `<picture>
  <source media="(prefers-color-scheme: dark)" srcset="${whiteUrl}">
  <img src="${blackUrl}" alt="${alt}"${classAttr}>
</picture>`;
}

/**
 * Create a simple img tag for a specific variation
 *
 * @param {string} clientName - Client identifier
 * @param {string} variation - Logo variation
 * @param {string} alt - Alt text
 * @param {string} cssClass - Optional CSS class
 * @returns {string} HTML <img> element
 *
 * @example
 * createLogoImg('crisis', 'white', 'Crisis Logo', 'logo')
 */
function createLogoImg(clientName, variation, alt, cssClass = '') {
  const url = getLogoUrl(clientName, variation);
  const classAttr = cssClass ? ` class="${cssClass}"` : '';

  return `<img src="${url}" alt="${alt}"${classAttr}>`;
}

/**
 * Preload logo images for faster rendering
 *
 * @param {string[]} clientNames - Array of client identifiers
 * @param {string[]} variations - Array of variations to preload (default: ['original', 'white', 'black'])
 *
 * @example
 * preloadLogos(['crisis', 'jp-morgan'], ['original', 'white']);
 */
function preloadLogos(clientNames, variations = ['original', 'white', 'black']) {
  const links = [];

  clientNames.forEach(clientName => {
    variations.forEach(variation => {
      const url = getLogoUrl(clientName, variation);
      const link = document.createElement('link');
      link.rel = 'preload';
      link.as = 'image';
      link.href = url;
      document.head.appendChild(link);
      links.push(link);
    });
  });

  return links;
}

/**
 * Batch fetch logo metadata from logo-urls.json
 *
 * @returns {Promise<Object>} Logo metadata including all clients and categories
 *
 * @example
 * const metadata = await getLogoMetadata();
 * console.log(metadata.clients['crisis'].urls.white);
 */
async function getLogoMetadata() {
  const metadataUrl = 'https://raw.githubusercontent.com/tobytotally/assets-library/main/docs/logo-urls.json';

  try {
    const response = await fetch(metadataUrl);
    if (!response.ok) {
      throw new Error(`Failed to fetch metadata: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching logo metadata:', error);
    return null;
  }
}

/**
 * Get all clients in a specific category
 *
 * @param {string} category - Category name: 'charity', 'commercial', 'technology', 'tools', 'accreditations'
 * @returns {Promise<string[]>} Array of client identifiers
 *
 * @example
 * const charityClients = await getClientsByCategory('charity');
 * // Returns: ['against-breast-cancer', 'crisis', 'gamcare', ...]
 */
async function getClientsByCategory(category) {
  const metadata = await getLogoMetadata();

  if (!metadata || !metadata.categories[category]) {
    console.warn(`Category "${category}" not found`);
    return [];
  }

  return metadata.categories[category].clients;
}

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    LOGO_BASE_URL,
    getLogoUrl,
    getAllLogoUrls,
    createResponsiveLogo,
    createLogoImg,
    preloadLogos,
    getLogoMetadata,
    getClientsByCategory
  };
}

// Make available globally in browser
if (typeof window !== 'undefined') {
  window.LogoHelper = {
    getLogoUrl,
    getAllLogoUrls,
    createResponsiveLogo,
    createLogoImg,
    preloadLogos,
    getLogoMetadata,
    getClientsByCategory
  };
}
