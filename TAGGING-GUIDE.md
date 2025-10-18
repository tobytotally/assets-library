# Client Logo Tagging Guide

## Overview
This document outlines the standardized tagging taxonomy for organizing client logos to support proposal automation and content management.

## Tag Categories

### 1. **Usage Context** (Where logos appear)
Tags that indicate where these logos are commonly used in proposals:

- `clients` - Featured client work/case studies
- `collaboration-tools` - Tools used in project delivery
- `technology-partner` - Technology partnerships and integrations
- `accreditation` - Certifications and accreditations
- `featured` - Highlighted/priority logos for prominent display

### 2. **Company Type / Industry**
Primary business sector or organization type:

#### Finance & Banking
- `finance`
- `banking`
- `fintech`
- `investment`
- `payments`

#### Healthcare & Social Care
- `healthcare`
- `social-care`
- `mental-health`
- `reproductive-health`
- `disability-support`

#### Technology & Digital
- `technology`
- `saas`
- `cybersecurity`
- `cloud-provider`
- `digital-platform`
- `digital-services`

#### Charity & Non-Profit
- `charity`
- `social-impact`
- `conservation`
- `social-services`
- `youth-support`
- `family-support`

#### Professional Services
- `legal`
- `consulting`
- `professional-services`
- `business-services`

#### Property & Construction
- `property`
- `construction`
- `residential`
- `infrastructure`

#### Media & Creative
- `media`
- `broadcasting`
- `podcasting`
- `marketing`
- `advertising`
- `creative-agency`
- `design`

#### Retail & Consumer
- `retail`
- `health-wellness`
- `fitness`
- `opticians`

#### Heritage & Culture
- `heritage`
- `museum`
- `arts-culture`
- `gardens`

#### Other Sectors
- `education`
- `government`
- `public-sector`
- `nhs`
- `emergency-services`
- `energy`
- `gambling`
- `entertainment`
- `sports`
- `travel`
- `leisure`

### 3. **Service Type**
Services provided or industry focus:

- `project-management`
- `time-tracking`
- `communication`
- `digital-marketing`
- `risk-management`
- `quality-improvement`
- `regulatory`
- `business-support`
- `referral-platform`
- `hosting`
- `smart-home`
- `signage`
- `manufacturing`
- `workspace`

### 4. **Special Attributes**

#### Project Characteristics
- `high-profile` - Well-known brands
- `international` - Global organizations
- `multilingual` - Multi-language projects
- `mobile-app` - Mobile application projects
- `wordpress` - WordPress implementations
- `custom-app` - Bespoke application development
- `cms-migration` - Content management system migrations
- `website-redesign` - Site redesign projects

#### Status & Priority
- `active-client` - Current active clients
- `featured` - Priority showcase clients
- `case-study` - Available for case study reference
- `needs-review` - Requires categorization/verification

#### Compliance & Standards
- `compliance` - Compliance-related
- `certification` - Official certifications
- `security` - Security certifications
- `accessibility` - Accessibility certifications/focus
- `diversity` - Diversity & inclusion initiatives

### 5. **Proposal Component Usage**
Tags indicating which proposal sections typically feature these logos:

- `accreditations` - Accreditation sections
- `clients` - Client work showcase
- `collaboration-tools` - Team collaboration section
- `technology-partner` - Technology stack section
- `case-study` - Case study components

## Usage Examples

### Example 1: Financial Services Client
```json
"jp-morgan": ["banking", "finance", "investment", "high-profile", "clients"]
```
**Use Case:** Include in proposals for other financial services clients, showcase high-profile client work

### Example 2: Collaboration Tool
```json
"slack": ["collaboration-tools", "communication", "saas", "technology-partner"]
```
**Use Case:** Include in "Our Technology Stack" sections, team collaboration descriptions

### Example 3: Healthcare Charity
```json
"crisis": ["charity", "homelessness", "social-impact", "featured", "clients", "case-study"]
```
**Use Case:** Include in charity sector proposals, social impact case studies, featured work sections

### Example 4: Accreditation
```json
"cyber-essentials-plus": ["accreditation", "security", "certification", "compliance"]
```
**Use Case:** Include in security/compliance sections, accreditation displays

## Proposal Automation Use Cases

### 1. **Sector-Specific Proposals**
Filter by industry tags to show relevant experience:
```javascript
// Show all healthcare clients
filterByTag("healthcare")

// Show charity + social-impact work
filterByTags(["charity", "social-impact"])
```

### 2. **Technology Stack Sections**
Automatically populate technology partner logos:
```javascript
filterByTag("technology-partner")
filterByTag("collaboration-tools")
```

### 3. **Accreditation Display**
Show all certifications:
```javascript
filterByTag("accreditation")
```

### 4. **Case Study Selection**
Find featured work in relevant sectors:
```javascript
filterByTags(["featured", "case-study", "finance"])
```

### 5. **High-Profile Client Showcase**
Display well-known brands:
```javascript
filterByTag("high-profile")
```

## Best Practices

### Tag Naming Conventions
- Use lowercase with hyphens (kebab-case)
- Be specific but not overly granular
- Use consistent terminology across similar clients
- Avoid abbreviations unless industry-standard

### Multiple Tags
- Apply 3-6 tags per client typically
- Always include: usage context + industry + type
- Add special attributes as relevant

### Maintenance
- Review and update tags quarterly
- Add new tags as needed for emerging categories
- Consolidate similar tags when possible
- Remove deprecated tags

## Quick Reference Tag List

### High-Frequency Tags (Most Commonly Used)
1. `clients` - Client work showcase
2. `charity` - Charity/non-profit organizations
3. `technology` - Technology companies
4. `finance` - Financial services
5. `healthcare` - Healthcare organizations
6. `commercial` - Commercial clients
7. `collaboration-tools` - Team collaboration tools
8. `technology-partner` - Technology partnerships
9. `accreditation` - Certifications/accreditations
10. `featured` - Priority showcase items

### Utility Tags
- `needs-review` - Requires attention/categorization
- `high-profile` - Well-known brands
- `case-study` - Available for case studies
- `active-client` - Current active engagement

## Import Instructions

To import the initial tag set into the Image Library:

1. Open `IMAGE-LIBRARY.html` in your browser
2. Open browser console (F12)
3. Fetch the initial tags file:
   ```javascript
   fetch('initial-client-tags.json')
     .then(r => r.json())
     .then(tags => {
       localStorage.setItem('clientTags', JSON.stringify(tags));
       location.reload();
     });
   ```
4. Or manually copy the contents of `initial-client-tags.json` and run:
   ```javascript
   importTags('paste-json-here');
   ```

## Export/Backup

To export your current tags for backup or sharing:
```javascript
exportTags(); // Downloads client-tags-export.json
```

---

**Last Updated:** 2025-10-18
**Total Clients:** 100
**Tag Categories:** 5 major categories
**Total Unique Tags:** ~80+ available tags
