# Briefly Frontend

A simple web interface for Briefly that analyzes text based on proven writing principles from multiple classic guides.

## Features

- **Real-time Analysis**: Instant feedback on your writing
- **11 Writing Principles**: Based on Wes Kao, Casagrande, Minto Pyramid, HBR Guide, and Zinsser
- **Clean Interface**: Modern, responsive design
- **Client-side Processing**: No server required - works entirely in the browser

## GitHub Pages Setup

To deploy this frontend to GitHub Pages:

1. **Push to GitHub**: 
   ```bash
   git add .
   git commit -m "Add Briefly frontend"
   git push origin main
   ```

2. **Enable GitHub Pages**:
   - Go to your repository settings
   - Scroll to "Pages" section
   - Select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Click "Save"

3. **Your site will be available at**: `https://yourusername.github.io/secondBrain`

## Files Structure

```
├── index.html          # Main HTML file
├── styles.css          # CSS styles
├── script.js           # JavaScript analysis logic
├── writing_bot.py      # Original Python bot (reference)
├── _config.yml         # GitHub Pages configuration
└── README-frontend.md  # This file
```

## How It Works

The frontend implements a simplified version of the Python bot's analysis logic directly in JavaScript. It analyzes text against 11 key writing principles:

1. **Super Specific How** - Focus on actionable implementation
2. **Cut Backstory** - Start right before you get eaten by the bear
3. **Clear Recommendations** - Be clear about your point of view
4. **Bottom Line First** - Lead with conclusions (Minto Pyramid)
5. **Sentence Structure** - Clear, concise sentences (Casagrande)
6. **Active Voice** - Prefer active over passive voice
7. **Logical Flow** - Structure arguments logically
8. **Conciseness** - Eliminate unnecessary words
9. **Clarity & Simplicity** - Write clearly, avoid jargon (Zinsser)
10. **Eliminate Clutter** - Remove unnecessary qualifiers (Zinsser)

## Customization

- **Styling**: Edit `styles.css` to change colors, fonts, or layout
- **Analysis Logic**: Modify `script.js` to add new rules or change existing ones
- **Content**: Update `index.html` to change descriptions or add new features

## Browser Support

The frontend uses modern JavaScript features and CSS, so it works best in:
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Contributing

Feel free to submit issues or pull requests to improve the frontend!
