# JSON-LD Schema Templates for GEO

Ready-to-use structured data templates optimized for AI discoverability.

---

## Organization (Required for All Businesses)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "Brief description of what the company does (50-160 characters).",
  "sameAs": [
    "https://en.wikipedia.org/wiki/Company_Name",
    "https://www.wikidata.org/wiki/Q12345",
    "https://www.linkedin.com/company/company-name",
    "https://www.youtube.com/@companyname",
    "https://twitter.com/companyname"
  ],
  "knowsAbout": [
    "Topic 1",
    "Topic 2",
    "Topic 3"
  ]
}
```

### Why sameAs Matters

The `sameAs` property tells AI systems: "This website IS the same entity as these profiles." This builds the entity graph that AI uses to verify and cite your content.

**Priority links:**
1. Wikipedia (highest authority)
2. Wikidata (machine-readable ID)
3. LinkedIn (business verification)
4. YouTube
5. Twitter/X

---

## WebSite + SearchAction (Homepage)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Site Name",
  "url": "https://example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

---

## LocalBusiness (Physical Locations)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "image": "https://example.com/photo.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main Street",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "telephone": "+1-555-555-5555",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "17:00"
    }
  ],
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 40.7128,
    "longitude": -74.0060
  },
  "priceRange": "$$",
  "sameAs": [
    "https://www.linkedin.com/company/company-name",
    "https://www.facebook.com/companyname"
  ]
}
```

---

## SoftwareApplication (SaaS)

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Product Name",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web, iOS, Android",
  "offers": {
    "@type": "Offer",
    "price": "29.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "description": "What the software does.",
  "featureList": [
    "Feature 1",
    "Feature 2",
    "Feature 3"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127"
  },
  "sameAs": [
    "https://twitter.com/productname",
    "https://www.linkedin.com/company/productname",
    "https://github.com/companyname"
  ]
}
```

---

## Product (E-commerce)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": "https://example.com/product.jpg",
  "description": "Product description.",
  "sku": "SKU123",
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/product",
    "price": "99.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "89"
  }
}
```

---

## Article (Publishers/Blog)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Headline",
  "image": "https://example.com/image.jpg",
  "datePublished": "2026-03-29T10:00:00Z",
  "dateModified": "2026-03-29T14:00:00Z",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/author/author-name",
    "sameAs": [
      "https://www.linkedin.com/in/authorname",
      "https://twitter.com/authorname"
    ],
    "jobTitle": "Senior Editor",
    "worksFor": {
      "@type": "Organization",
      "name": "Publication Name"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "Publication Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "description": "Article description (150-160 characters recommended).",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".article-summary", ".lead-paragraph"]
  }
}
```

### Author Schema (E-E-A-T Signal)

Author schema is critical for AI trust. Include:
- Full name
- Author page URL on your site
- LinkedIn profile
- Job title and organization
- Areas of expertise (knowsAbout)
- Awards or credentials

---

## FAQPage (Questions & Answers)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is your return policy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We offer a 30-day return policy for all unused items in original packaging."
      }
    },
    {
      "@type": "Question",
      "name": "How do I contact support?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can reach our support team at support@example.com or call 1-555-555-5555."
      }
    }
  ]
}
```

---

## BreadcrumbList (Navigation)

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Category",
      "item": "https://example.com/category"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Current Page",
      "item": "https://example.com/category/page"
    }
  ]
}
```

---

## Person (Thought Leaders/Authors)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Full Name",
  "url": "https://example.com/about/name",
  "image": "https://example.com/photo.jpg",
  "jobTitle": "CEO / Founder",
  "worksFor": {
    "@type": "Organization",
    "name": "Company Name"
  },
  "description": "Brief bio (1-2 sentences).",
  "sameAs": [
    "https://www.linkedin.com/in/username",
    "https://twitter.com/username",
    "https://github.com/username",
    "https://scholar.google.com/citations?user=ID"
  ],
  "knowsAbout": [
    "Expertise Area 1",
    "Expertise Area 2"
  ],
  "alumniOf": [
    {
      "@type": "CollegeOrUniversity",
      "name": "University Name"
    }
  ]
}
```

---

## Implementation Tips

### Where to Place JSON-LD

- Put in `<head>` section of HTML
- NOT in body
- NOT injected via JavaScript (AI crawlers may miss it)

### Validation

- Use [Google Rich Results Test](https://search.google.com/test/rich-results)
- Use [Schema.org Validator](https://validator.schema.org/)

### Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| JSON-LD in body | May not be detected | Move to `<head>` |
| JS-injected schema | Delayed/not found | Server-side render |
| Invalid JSON syntax | Validation fails | Check for trailing commas |
| Missing required props | Incomplete entity | Add all required fields |
| No sameAs | Weak entity | Add 3-5 platform links |

### Priority Order

1. **Organization** - Always required
2. **WebSite + SearchAction** - Homepage
3. **Business type** - LocalBusiness, Product, SoftwareApplication, Article
4. **Author** - For publisher content
5. **FAQ** - For Q&A content
6. **Breadcrumb** - Inner pages
