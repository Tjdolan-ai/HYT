# 🌟 HolyTechAI: The Wardrobe in the Machine

> *"The task of the modern educator is not to cut down jungles, but to irrigate deserts."* — C.S. Lewis

## 📖 Vision: Sacred Futurism

HolyTechAI exists at the intersection of ancient wisdom and emerging technology. We're building more than an affiliate platform—we're creating a **digital sanctuary** where the Church can discover, evaluate, and ethically implement AI tools without losing its soul.

Our mission: To be the **Narnia wardrobe** of the AI age—a portal that leads not to synthetic substitutes, but to deeper truth.

## 🎯 What We're Building

HolyTechAI is a faith-tech platform that:
- 🔍 **Evaluates** AI tools through a theological lens
- 📚 **Educates** churches on ethical AI implementation
- 🛡️ **Protects** believers from digital idolatry
- 💡 **Empowers** ministries with vetted technologies
- 🤝 **Connects** faith communities with sacred-aligned innovation

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ 
- WordPress 6.0+ or Static Site Generator
- Git
- Google Analytics account
- ConvertKit account (for email capture)

### Installation

```bash
# Clone the repository
git clone https://github.com/Tjdolan-ai/HYT.git
cd HYT

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys and configuration

# Run development server
npm run dev

# Build for production
npm run build
```

### Environment Variables

```env
# API Keys
GEMINI_API_KEY=your_gemini_key
CONVERTKIT_API_KEY=your_convertkit_key
GA_MEASUREMENT_ID=your_ga_id

# Affiliate Programs
JASPER_AFFILIATE_ID=your_jasper_id
FAITHGPT_AFFILIATE_ID=your_faithgpt_id

# WordPress (if using)
WP_API_URL=https://yourdomain.com/wp-json
```

## 📁 Project Structure

```
HYT/
├── 📄 README.md              # You are here
├── 📄 LICENSE               # Non-commercial license
├── 📄 package.json          # Dependencies
├── 🌐 public/              # Static assets
│   ├── index.html
│   └── assets/
├── 💻 src/                 # Source code
│   ├── components/         # React/Vue components
│   │   ├── AIChat/        # Interactive AI demos
│   │   ├── DevotionalGen/ # Devotional generator
│   │   └── AffiliateCTA/  # Call-to-action components
│   ├── content/           # Markdown content
│   │   ├── pillars/       # Comprehensive guides
│   │   ├── clusters/      # Supporting articles
│   │   └── devotionals/   # AI-assisted devotions
│   ├── templates/         # Content templates
│   │   ├── screwtape.md   # Lewis-style satire
│   │   ├── parable.md     # Theological stories
│   │   └── review.md      # Product evaluations
│   └── utils/            # Helper functions
├── 🔌 api/               # Backend endpoints
│   ├── gemini/           # Gemini AI integration
│   └── devotional/       # Devotional API
└── 🚀 deploy/           # Deployment configs
```

## 📅 90-Day Launch Roadmap

### Month 1: Foundations (Weeks 1-4)
- ✅ Set up WordPress/CMS infrastructure
- ✅ Implement SEO foundation (RankMath/Yoast)
- ✅ Create pillar content: "Christian AI Tools Guide"
- ✅ Integrate affiliate management (ThirstyAffiliates)
- ✅ Launch email capture with ConvertKit

### Month 2: Devotion & Discernment (Weeks 5-8)
- 🔄 Build DevotionalAI generator
- 🔄 Create interactive prayer tools
- 🔄 Launch "Digital Discipleship" email course
- 🔄 Implement community features

### Month 3: Ethics & The Future (Weeks 9-12)
- 📋 Release Sanctuary OS™ beta
- 📋 Publish theological framework
- 📋 Launch comprehensive resource hub
- 📋 Full platform optimization

## 🎨 Content Guidelines

### The Lewis Voice
Every piece should embody:
- **Clarity over complexity** - Make the profound accessible
- **Story over statistics** - Lead with narrative, support with data
- **Wonder over cynicism** - Maintain childlike curiosity about technology
- **Truth over trends** - Anchor in eternal principles

### Content Types
1. **🏛️ Pillars** - Comprehensive guides (3,000+ words)
2. **🌿 Clusters** - Supporting articles (1,500+ words)
3. **📺 Videos** - Script-first approach
4. **😈 Screwtape Satires** - Modern temptations exposed
5. **🙏 Devotionals** - AI-assisted, human-verified

## 🤖 AI Integration Philosophy

**"Tool, Not Oracle"** - Our Core Principle

```javascript
// Example: Devotional Generator Ethics
const generateDevotional = async (theme) => {
  const aiDraft = await geminiAPI.generate(theme);
  
  // ALWAYS require human review
  return {
    content: aiDraft,
    status: 'PENDING_REVIEW',
    disclaimer: 'AI-assisted draft requires pastoral review'
  };
};
```

## 📊 Success Metrics

### Technical KPIs
- 🎯 **Page Speed**: < 3s load time
- 🎯 **Core Web Vitals**: All green
- 🎯 **Mobile Score**: 95+ on PageSpeed Insights

### Ministry KPIs
- 💚 **Engagement**: Comments focus on spiritual growth
- 💚 **Trust**: Theological accuracy rating > 95%
- 💚 **Impact**: Testimonials of transformed ministries

### Business KPIs
- 💰 **Traffic**: 50,000 monthly visitors by Month 6
- 💰 **Conversion**: 3% email signup rate
- 💰 **Revenue**: $10,000/month affiliate income by Month 12

## 🛠️ Development Workflow

```bash
# Feature branch workflow
git checkout -b feature/devotional-generator
# Make changes
git add .
git commit -m "feat: add AI devotional generator with pastoral review"
git push origin feature/devotional-generator
# Create PR with theological review requirement
```

## 🤝 Contributing

We welcome contributions that align with our Sacred Futurism vision!

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Contribution Guidelines
- ✅ All content must pass theological review
- ✅ Code must include appropriate error handling
- ✅ AI integrations must maintain "Tool, Not Oracle" principle
- ✅ Affiliate links must include proper disclosures

## 📚 Resources

### Internal Documentation
- 📄 [The Wardrobe in the Machine Blueprint](./docs/wardrobe-blueprint.pdf)
- 📄 [Faith + AI SEO Analysis](./docs/seo-analysis.md)
- 📄 [Sacred Futurism Manifesto](./docs/sacred-futurism.md)

### External Resources
- 🔗 [C.S. Lewis on Technology](https://www.cslewisinstitute.org)
- 🔗 [Ethical AI Guidelines](https://www.vatican.va/roman_curia/pontifical_academies/acdlife/documents/rc_pont-acd_life_doc_20200228_rome-call-for-ai-ethics_en.html)
- 🔗 [Church Tech Today](https://churchtechtoday.com)

## 🙏 Theological Advisory Board

Special thanks to our advisors ensuring doctrinal soundness:
- *Positions to be filled*
- *Currently accepting applications from seminary professors*

## 📄 License

This project is licensed under a custom non-commercial license - see the [LICENSE](LICENSE) file for details. Commercial use requires explicit permission.

## 🌟 Join the Journey

> *"There are no ordinary people. You have never talked to a mere mortal."* — C.S. Lewis

Every line of code, every article, every feature we build serves an eternal purpose. We're not just building a website—we're crafting a digital cathedral where technology serves transcendence.

Ready to step through the wardrobe? Let's build something sacred together.

---

**🚀 Launch Status**: Pre-launch (Target: October 2025)  
**💬 Contact**: hello@holytechai.com  
**🐦 Twitter**: [@HolyTechAI](https://twitter.com/holytechai)  
**📧 Newsletter**: [Subscribe for Sacred Futurism insights](https://holytechai.com/newsletter)

*"Further up and further in!"* 🦁✨
