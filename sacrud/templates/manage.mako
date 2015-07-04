<%inherit file="_base.mako"/>

<div class="control">
  <a href="${model.__name__}/add">+</a>
</div>

% if objects:
<div class="object-list">
  <ul>
    % for obj in objects:
    <li>
      <a href="${model.__name__}/edit/%{obj.id}">
	${unicode(obj)}
      </a>
    </li>
    % endfor
  </ul>
</div>
% endif
