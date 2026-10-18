/* Remove optional ChatGPT link attribution from this site's visible URL.
   This does not affect referrer headers or other query parameters. */
(() => {
  try {
    const url = new URL(window.location.href);
    let changed = false;
    for (const key of ["source", "utm_source"]) {
      if ((url.searchParams.get(key) || "").toLowerCase() === "chatgpt.com") {
        url.searchParams.delete(key);
        changed = true;
      }
    }
    if (changed) {
      window.history.replaceState(
        window.history.state,
        "",
        url.pathname + url.search + url.hash
      );
    }
  } catch (_error) {
    // Navigation remains fully functional if the browser disallows rewriting.
  }
})();
