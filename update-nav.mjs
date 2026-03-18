import { readFileSync, writeFileSync } from 'fs';

// Pages that need nav updates (not index.html - already done, not new pages - agents handle those)
const pages = [
    'styles.html',
    'colors.html',
    'typography.html',
    'charts.html',
    'ux-guidelines.html',
    'patterns.html',
    'reasoning.html'
];

// Map page filename to which nav item should be active
const activeMap = {
    'styles.html': { type: 'primary', href: 'styles.html' },
    'colors.html': { type: 'primary', href: 'colors.html' },
    'typography.html': { type: 'primary', href: 'typography.html' },
    'charts.html': { type: 'primary', href: 'charts.html' },
    'ux-guidelines.html': { type: 'more', href: 'ux-guidelines.html' },
    'patterns.html': { type: 'more', href: 'patterns.html' },
    'reasoning.html': { type: 'more', href: 'reasoning.html' },
};

const primaryLinks = ['styles.html', 'colors.html', 'typography.html', 'charts.html', 'products.html', 'icons.html'];
const primaryNames = ['Styles', 'Colors', 'Typography', 'Charts', 'Products', 'Icons'];
const moreLinks = ['stacks.html', 'ux-guidelines.html', 'patterns.html', 'reasoning.html', 'react-performance.html', 'web-interface.html'];
const moreNames = ['Stacks', 'UX Guidelines', 'Patterns', 'Reasoning', 'React Perf', 'Web Interface'];
const allLinks = [...primaryLinks, ...moreLinks];
const allNames = [...primaryNames, ...moreNames];

function buildDesktopNav(activeHref) {
    let html = '            <div class="hidden md:flex items-center gap-1">\n';

    // Primary links
    for (let i = 0; i < primaryLinks.length; i++) {
        const isActive = primaryLinks[i] === activeHref;
        if (isActive) {
            html += `                <a href="${primaryLinks[i]}" class="px-3 py-2 text-sm text-white bg-white/10 transition-colors rounded-lg">${primaryNames[i]}</a>\n`;
        } else {
            html += `                <a href="${primaryLinks[i]}" class="px-3 py-2 text-sm text-gray-400 hover:text-white transition-colors rounded-lg hover:bg-white/5">${primaryNames[i]}</a>\n`;
        }
    }

    // More dropdown
    html += '                <div class="relative">\n';
    html += '                    <button onclick="document.getElementById(\'more-menu\').classList.toggle(\'hidden\')" class="px-3 py-2 text-sm text-gray-400 hover:text-white transition-colors rounded-lg hover:bg-white/5 inline-flex items-center gap-1">More <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button>\n';
    html += '                    <div id="more-menu" class="hidden absolute right-0 top-full mt-2 w-52 bg-[#12131A] border border-white/10 rounded-xl shadow-2xl py-2 z-50">\n';

    for (let i = 0; i < moreLinks.length; i++) {
        const isActive = moreLinks[i] === activeHref;
        if (isActive) {
            html += `                        <a href="${moreLinks[i]}" class="block px-4 py-2 text-sm text-white bg-white/10 rounded-lg mx-2">${moreNames[i]}</a>\n`;
        } else {
            html += `                        <a href="${moreLinks[i]}" class="block px-4 py-2 text-sm text-gray-400 hover:text-white hover:bg-white/5">${moreNames[i]}</a>\n`;
        }
    }

    html += '                    </div>\n';
    html += '                </div>\n';
    html += '            </div>';
    return html;
}

function buildMobileMenu(activeHref) {
    let html = '        <div id="mobile-menu" class="hidden md:hidden border-t border-white/5 px-6 py-4 space-y-2">\n';
    for (let i = 0; i < allLinks.length; i++) {
        const isActive = allLinks[i] === activeHref;
        if (isActive) {
            html += `            <a href="${allLinks[i]}" class="block px-3 py-2 text-sm text-white bg-white/10 rounded-lg">${allNames[i]}</a>\n`;
        } else {
            html += `            <a href="${allLinks[i]}" class="block px-3 py-2 text-sm text-gray-400 hover:text-white rounded-lg hover:bg-white/5">${allNames[i]}</a>\n`;
        }
    }
    html += '        </div>';
    return html;
}

function buildFooter() {
    return `                <div class="flex flex-wrap justify-center gap-4 text-sm text-gray-500">
                    <a href="styles.html" class="hover:text-white transition-colors">Styles</a>
                    <a href="colors.html" class="hover:text-white transition-colors">Colors</a>
                    <a href="typography.html" class="hover:text-white transition-colors">Typography</a>
                    <a href="charts.html" class="hover:text-white transition-colors">Charts</a>
                    <a href="products.html" class="hover:text-white transition-colors">Products</a>
                    <a href="icons.html" class="hover:text-white transition-colors">Icons</a>
                    <a href="stacks.html" class="hover:text-white transition-colors">Stacks</a>
                    <a href="ux-guidelines.html" class="hover:text-white transition-colors">UX Guidelines</a>
                    <a href="patterns.html" class="hover:text-white transition-colors">Patterns</a>
                    <a href="reasoning.html" class="hover:text-white transition-colors">Reasoning</a>
                    <a href="react-performance.html" class="hover:text-white transition-colors">React Perf</a>
                    <a href="web-interface.html" class="hover:text-white transition-colors">Web Interface</a>
                </div>`;
}

const dropdownScript = `<script>document.addEventListener('click',e=>{if(!e.target.closest('#more-menu')&&!e.target.closest('[onclick*="more-menu"]')){document.getElementById('more-menu')?.classList.add('hidden')}})</script>`;

for (const page of pages) {
    let content = readFileSync(page, 'utf8');
    const activeHref = page;

    // Replace desktop nav
    const desktopNavRegex = /\s*<div class="hidden md:flex items-center gap-1">[\s\S]*?<\/div>\s*(?=<button onclick="document\.getElementById\('mobile-menu'\))/;
    const newDesktopNav = '\n' + buildDesktopNav(activeHref) + '\n';
    content = content.replace(desktopNavRegex, newDesktopNav);

    // Replace mobile menu
    const mobileMenuRegex = /\s*<div id="mobile-menu" class="hidden md:hidden[^"]*"[\s\S]*?<\/div>\s*(?=<\/nav>)/;
    const newMobileMenu = '\n' + buildMobileMenu(activeHref) + '\n';
    content = content.replace(mobileMenuRegex, newMobileMenu);

    // Replace/update footer links
    // Look for the footer links div pattern
    const footerLinksRegex = /<div class="flex[^"]*text-sm text-gray-500">[\s\S]*?<\/div>(?=\s*<div class="text-sm text-gray-600">)/;
    if (footerLinksRegex.test(content)) {
        content = content.replace(footerLinksRegex, buildFooter());
    }

    // Also handle simpler footer patterns (like ux-guidelines.html's centered footer)
    // These don't have the same structure so we skip them for now

    // Add dropdown close script if not present
    if (!content.includes('more-menu')) {
        // Script already added via nav replacement
    }
    if (!content.includes("document.addEventListener('click',e=>{if(!e.target.closest('#more-menu')")) {
        content = content.replace('</body>', dropdownScript + '\n</body>');
    }

    // Add ?q= URL param support to search inputs
    if (content.includes('id="search-input"') || content.includes('id="searchInput"')) {
        const searchInputId = content.includes('id="searchInput"') ? 'searchInput' : 'search-input';

        // Check if ?q= support already exists
        if (!content.includes("URLSearchParams")) {
            const qParamScript = `
// URL param support
const urlParams = new URLSearchParams(window.location.search);
const qParam = urlParams.get('q');
if (qParam) {
    document.getElementById('${searchInputId}').value = qParam;
    searchQuery = qParam.toLowerCase();
    ${content.includes('renderGuidelines') ? 'renderGuidelines()' :
      content.includes('renderPalettes') ? 'renderPalettes()' :
      content.includes('renderCards') ? 'renderCards()' :
      content.includes('renderPatterns') ? 'renderPatterns()' :
      content.includes('renderStyles') ? 'renderStyles()' :
      content.includes('renderAll') ? 'renderAll()' :
      content.includes('filterAndRender') ? 'filterAndRender()' :
      'render()'}
}`;
            // Insert before </script> at end
            const lastScriptEnd = content.lastIndexOf('</script>');
            if (lastScriptEnd > 0) {
                content = content.slice(0, lastScriptEnd) + qParamScript + '\n' + content.slice(lastScriptEnd);
            }
        }
    }

    writeFileSync(page, content, 'utf8');
    console.log(`Updated: ${page}`);
}

console.log('All pages updated!');
