---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
header:
  og_image: "research/ecdf.png"
---

The overarching theme in my research is flow and transport of fluids/tracers through fractured rock. 

If you would like to reach to me about potential collaboration, please use my email provided in the sidebar.

<nbsp>

{% include base_path %}

{% assign ordered_pages = site.research | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}

