<%inherit file="_base.mako"/>

% if models:
<ul>
  % for model in sorted(models):
  <li>
    <a href="/manage/${model.__name__}">
      ${model.__name__}
    </a>
  </li>
  % endfor
</ul>
% endif
